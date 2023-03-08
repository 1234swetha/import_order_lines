from odoo import models, fields, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError


class ImportLineWizard(models.TransientModel):
    _name = "import.line.wizard"
    _description = 'Import Line Wizard'

    file = fields.Binary(string="Xls sheet")
    sale_id = fields.Many2one('sale.order')

    def import_order_line(self):
        try:
            wb = openpyxl.load_workbook(filename=BytesIO(base64.b64decode(self.file)), read_only=True)
            ws = wb.active
            for record in ws.iter_rows(min_row=2, max_row=None, min_col=None, max_col=None, values_only=True):
                search = self.env['product.product'].search([('name', '=', record[0])])
                uom_search = self.env['uom.uom'].search([('name', '=', record[2])])
                if not search:
                    search = self.env['product.product'].create({'name': record[0]})
                if not uom_search:
                    uom_search = self.env['product.product'].browse([1])
                self.sale_id.order_line = [(0, 0, {
                    'product_id': search.id,
                    'product_uom_qty': record[1],
                    'product_uom': uom_search.id,
                    'name': record[3],
                    'price_unit': record[4]
                })]
                self.sale_id.imported = True
        except:
            raise UserError(_('Please insert a valid file'))

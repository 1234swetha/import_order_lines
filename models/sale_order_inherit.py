from odoo import models, fields


class SaleInherit(models.Model):
    _inherit = "sale.order"

    imported = fields.Boolean()

    def import_lines(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Import',
            'view_mode': 'form',
            'res_model': 'import.line.wizard',
            'target': 'new',
            'context': {'default_sale_id': self.id}
        }


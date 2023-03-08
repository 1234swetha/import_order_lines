{
    'name': 'Import Order lines',
    'version': '16.0.1.0.0',
    'sequence': 1,
    'depends': [
        'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_inherit_views.xml',
        'wizard/import_line_wizard.xml'
    ]
}

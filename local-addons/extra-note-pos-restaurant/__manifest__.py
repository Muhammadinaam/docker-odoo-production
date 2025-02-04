# -*- coding: utf-8 -*-
{
    'name': "extra-note-pos-restaurant",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '15.1',

    # any module necessary for this one to work correctly
    'depends': ['pos_restaurant', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'extra-note-pos-restaurant/static/src/js/extranote_button.js',
        ],
        'web.assets_qweb': [
            'extra-note-pos-restaurant/static/src/xml/**/*',
        ],
    },
}

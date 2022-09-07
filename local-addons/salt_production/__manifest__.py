# -*- coding: utf-8 -*-
{
    'name': "Salt Production",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Akonto Solutions",
    'website': "http://www.akonto.ltd",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'report/refine_report.xml',
        # 'report/report.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/rawsalt.xml',
        'views/productionconsume.xml',
        'views/burnerconsume.xml',
        'views/templates.xml',
        'views/weather_menu.xml',
        'views/refine.xml',
        'views/circuit.xml',
        'views/analysisreport.xml',
        'views/washing.xml',
        'views/projectedprod.xml',
        'views/widthsaltplates.xml',
        'views/pump.xml',
        'views/testingmethod.xml',
        'views/circuittwo.xml',
        'views/feedevaporator.xml',
        'views/views.xml',
        'views/reports.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'salt_production/static/src/css/my.css',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': '-100',
    'application': True,
}

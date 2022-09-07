# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "POS Product Bundle BOM",
    "version" : "15.0.0.0",
    "category" : "Point of Sale",
    'summary': 'BOM for pos product bom pos bom for point of sale product bom point of sale product bundle bom pos bundle bom pos product item bom pos combo bom pos combo bundle pos product bundle pos bundle combo pos product combo pos bom bundle pos Ingredients on pos',
    "description": """
    
    This odoo app helps user to create and sell POS product like BOM, User can add sub products or components with it having different unit of measure, Customer can place order for this POS BOM product and transfer will created with all components products added into BOM product. 
    
    """,
    "author": "BrowseInfo",
    "website" : "https://www.browseinfo.in",
    "price": 39,
    "currency": 'EUR',
    "depends" : ['base','point_of_sale','stock','account'],
    "data": [
        'security/ir.model.access.csv',
        'views/product_product.xml',
        'views/bom_product_product_view.xml',
    ],

    "auto_install": False,
    "installable": True,
    "live_test_url":'https://youtu.be/1CminlVKkKw',
    "images":['static/description/Banner.png'],
    'license': 'OPL-1'
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

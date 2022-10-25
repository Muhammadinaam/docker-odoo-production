# -*- coding: utf-8 -*-
######################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2021-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Mashood K.U (Contact : odoo@cybrosys.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#    or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
########################################################################################
{
    'name': "POS Order Types",
    'version': '15.0.1.0.0',
    'summary': """ Helps the salesman to specify the type of order like parcel, delivery etc.""",
    'description': """This module helps to choose the order types in POS screen. You have the option to choose 
                        different order types for multiple Point of Sale.""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'Point of Sale',
    'depends': ['pos_restaurant', 'point_of_sale'],
    'website': 'http://www.akonto.ltd',
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv'
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_order_types/static/src/js/models.js',
            'pos_order_types/static/src/js/deliverymethod_button.js',
        ],
        'web.assets_qweb': [
            'pos_order_types/static/src/xml/**/*',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'price': 9.99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': True,
}

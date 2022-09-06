# -*- coding: utf-8 -*-
# from odoo import http


# class SaltProduction(http.Controller):
#     @http.route('/salt_production/salt_production', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salt_production/salt_production/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('salt_production.listing', {
#             'root': '/salt_production/salt_production',
#             'objects': http.request.env['salt_production.salt_production'].search([]),
#         })

#     @http.route('/salt_production/salt_production/objects/<model("salt_production.salt_production"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salt_production.object', {
#             'object': obj
#         })

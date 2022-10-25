# -*- coding: utf-8 -*-
# from odoo import http


# class Extra-note-pos-restaurant(http.Controller):
#     @http.route('/extra-note-pos-restaurant/extra-note-pos-restaurant', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-note-pos-restaurant/extra-note-pos-restaurant/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-note-pos-restaurant.listing', {
#             'root': '/extra-note-pos-restaurant/extra-note-pos-restaurant',
#             'objects': http.request.env['extra-note-pos-restaurant.extra-note-pos-restaurant'].search([]),
#         })

#     @http.route('/extra-note-pos-restaurant/extra-note-pos-restaurant/objects/<model("extra-note-pos-restaurant.extra-note-pos-restaurant"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-note-pos-restaurant.object', {
#             'object': obj
#         })

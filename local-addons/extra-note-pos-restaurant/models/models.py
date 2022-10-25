# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class extra-note-pos-restaurant(models.Model):
#     _name = 'extra-note-pos-restaurant.extra-note-pos-restaurant'
#     _description = 'extra-note-pos-restaurant.extra-note-pos-restaurant'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

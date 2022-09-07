from odoo import models, fields, api
from datetime import datetime


class CircuitTwoPost(models.Model):
    _name = 'circuittwo.post'
    _description = 'Circuit Two data'
    # _rec_name = 'date'


    
    crystalizer_id = fields.Many2one("salt_production.crystalizer", string="Crystaliser" ,required=True)
    time = fields.Datetime(string="Time")
    btm = fields.Float(string="Bottom Level")
    top = fields.Float(string="Top Level")
    height= fields.Float(string="Height " , compute="_compute_total" , readonly="1")
    temp = fields.Float(string="Temperature (C)")
    density = fields.Float(string="density")
    remark = fields.Char(string="Obeservations - Remarks")



    @api.depends("btm")
    def _compute_total(self):
        for record in self:
            record.height = record.top - record.btm


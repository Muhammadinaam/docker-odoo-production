from odoo import models, fields, api
from datetime import datetime
from datetime import time


class CircuitPost(models.Model):
    _name = 'circuit.post'
    _description = 'circuit data Post model'

 
    
    water_container_id = fields.Many2one("salt_production.water_container", string="Evaporator",required=True)
    time = fields.Datetime(string="Time" ,required=True)
    btm = fields.Float(string="Water Bottom LVL")
    top = fields.Float(string="Water Top LVL")
    height= fields.Float(string="Height of water" , compute="_compute_total" , readonly="1")
    h_woodenbarrier = fields.Float(string="Height of Wooden Barrier")
    brine_overflow = fields.Float(string="Brine OverFlow (cm)" ,compute="_compute_brine_height" , readonly="1")
    no_woodenbarrier = fields.Integer(string="No of Wooden Barrier")
    temp = fields.Float(string="Temperature (C)")
    density = fields.Float(string="density")
    ntu = fields.Float(string="NTU")
    remark = fields.Char(string="Obeservations - Remarks")



    @api.depends("btm")
    def _compute_total(self):
        for record in self:
            record.height = record.top - record.btm

    @api.depends("height")
    def _compute_brine_height(self):
        for record in self:
            record.brine_overflow = record.height - record.h_woodenbarrier
    
    
        
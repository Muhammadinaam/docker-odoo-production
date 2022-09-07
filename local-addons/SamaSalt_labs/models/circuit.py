from odoo import models, fields, api


class CircuitPost(models.Model):
    _name = 'circuit.post'
    _description = 'circuit data Post  model'


    weather_id = fields.Many2one("weather.post", string="date")
    # wind = fields.Char(related=weather_id.date, string="weather")



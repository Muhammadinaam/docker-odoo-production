from odoo import models, fields, api


class WeatherPost(models.Model):
    _name = 'weather.post'
    _description = 'weather post data'
    _rec_name = 'date'


    date = fields.Date(string="Date", default=fields.Date.context_today)
    time = fields.Datetime(string="Time")

    tempC = fields.Integer(string="Temprature C")
    humidity = fields.Integer(string="Humidity %")
    windspeed = fields.Integer(string="Windspeed km/h")
    windDirection = fields.Char(string="Wind Direction")
    rainfall = fields.Integer(string="Rain Fall (mm)")
    beaufort = fields.Integer(string="Beaufort 1to12")
    evaporation = fields.Integer(string="Evaporation")


    # @api.multi
    # def name_get(self):
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s - %s' % (rec.weather_id, rec.date)))
    #     return res
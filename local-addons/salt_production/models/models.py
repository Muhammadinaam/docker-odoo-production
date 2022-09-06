from odoo import models, fields, api


class WaterPump(models.Model):
    _name = 'salt_production.water_pump'
    _description = 'salt_production.water_pump'

    code = fields.Char(required=True)
    name = fields.Char(required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name already exists!"),
        ('code_uniq', 'unique (code)', "Code already exists!"),
    ]

    def write(self, vals):
        # raise Exception('hello')
        print('hello hello')
        return super().write(vals)


class WaterContainer(models.Model):
    _name = 'salt_production.water_container'
    _description = 'salt_production.water_container'

    code = fields.Char(required=True)
    name = fields.Char(required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name already exists!"),
        ('code_uniq', 'unique (code)', "Code already exists!"),
    ]


class Crystalizer(models.Model):
    _name = 'salt_production.crystalizer'
    _description = 'salt_production.crystalizer'

    code = fields.Char(required=True)
    name = fields.Char(required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name already exists!"),
        ('code_uniq', 'unique (code)', "Code already exists!"),
    ]

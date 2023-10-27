from odoo import api, models, fields

class Shinra(models.Model):
    _name = 'final_fantasy.shinra'
    name = fields.Char()
    fecha_nacimiento = fields.Date(required=True)

class Turco(models.Model):
    _name = 'final_fantasy.turco'
    name = fields.Char()
    fecha_nacimiento = fields.Date(required=True)
    rango = fields.Char()

class Soldado(models.Model):
    _name = 'final_fantasy.soldado'
    fecha_nacimiento = fields.Date(required=True)



    
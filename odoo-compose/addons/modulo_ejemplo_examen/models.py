from odoo import api, models, fields

class Shinra(models.Model):
    _name = 'final_fantasy.shinra'
    name = fields.Char()
    fecha_nacimiento = fields.Date(required=True)




    
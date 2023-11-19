from odoo import api, models, fields

class Shinra(models.Model):
    _name = 'finalfantasy.shinra'
    _description = 'Shira'
    name = fields.Char(string="Nombre")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
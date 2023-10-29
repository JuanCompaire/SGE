from odoo import api, models, fields

class Cliente(models.Model):
    _name = 'veterinaria.cliente'
    name = fields.Char()
    fecha_inscripcion = fields.Date(required=True)
    cod_mascotas = fields.One2Many(comodel_name='veterinaria.mascota', inverse_name='cod_cliente')

class Mascota(models.Model):
    _name = 'veterinaria.mascota'
    name = fields.Char()
    tipo = fields.Char()
    cod_cliente = fields.Many2One(comodel_name='veterinaria.cliente', inverse_name='cod_mascotas')

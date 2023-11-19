from odoo import api, models, fields

class Shinra(models.Model):
    _name = 'finalfantasy.shinra'
    _description = 'Shira'
    name = fields.Char(string="Nombre")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)

class Turco(models.Model):
    _name = 'finalfantasy.turco'
    _description = 'Turco'
    name = fields.Char(string="Nombre")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    rango = fields.Char(string="Rango")

class Soldado(models.Model):
    _name = 'finalfantasy.soldado'
    _description = 'Soldado'
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    clase = fields.Selection([
        ('Primera', 'primera'),
        ('Segunda', 'segunda')        
        ], string="Clase")
    arma_id = fields.Many2one(comodel_name='finalfantasy.arma', inverse_name='soldado_id', string="Arma")
    
class Arma(models.Model):
    _name = 'finalfantasy.arma'
    _description = 'Arma'
    name = fields.Char(string="Nombre")
    material_fabricacion = fields.Char(string="Material de fabricación")
    numero_ranuras_materia = fields.Integer(string="Número de ranuras de materia")
    soldado_id = fields.One2many(comodel_name='finalfantasy.soldado', inverse_name='arma_id')
    materia_id = fields.One2many(comodel_name='finalfantasy.materia', inverse_name='arma_id', string="Materia")

class Materia(models.Model):
    _name = 'finalfantasy.materia'
    _description = 'Materia'
    name = fields.Char(string="Nombre")
    tipo = fields.Selection([
        ('Magia negra', 'magia negra'),
        ('Invocacion', 'invocacion'),
        ('Apoyo', 'apoyo'),
        ], string="Tipo")
    numero_ranuras = fields.Integer(string="Número de ranuras")
    arma_id = fields.Many2one(comodel_name='finalfantasy.arma', inverse_name='materia_id', string="Arma")
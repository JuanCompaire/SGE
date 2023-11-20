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
    avalancha_id = fields.One2many(comodel_name='finalfantasy.avalancha', inverse_name='turco_id', string="Avalancha")

class Soldado(models.Model):
    _name = 'finalfantasy.soldado'
    _description = 'Soldado'
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    clase = fields.Selection([
        ('Primera', 'primera'),
        ('Segunda', 'segunda')        
        ], string="Clase")
    arma_id = fields.Many2one(comodel_name='finalfantasy.arma', inverse_name='soldado_id', string="Arma")
    indice_locura = fields.Integer(string="Índice de locura")


    
class Arma(models.Model):
    _name = 'finalfantasy.arma'
    _description = 'Arma'
    name = fields.Char(string="Nombre")
    material_fabricacion = fields.Char(string="Material de fabricación")
    numero_ranuras_materia = fields.Integer(string="Número de ranuras de materia")
    soldado_id = fields.One2many(comodel_name='finalfantasy.soldado', inverse_name='arma_id')
    materia_id = fields.Many2many(comodel_name='finalfantasy.materia', inverse_name='arma_id', string="Materia")
    avalancha_id = fields.One2many(comodel_name='finalfantasy.avalancha', inverse_name='arma_id', string="Avalancha")

   

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
    arma_id = fields.Many2many(comodel_name='finalfantasy.arma', inverse_name='materia_id', string="Arma")

class Avalancha(models.Model):
    _name = 'finalfantasy.avalancha'
    _description = 'Avalancha'
    name = fields.Char(string="Nombre")
    arma_id = fields.Many2one(comodel_name='finalfantasy.arma', inverse_name='avalancha_id', string="Arma")
    antiguo_soldado = fields.Boolean(string="Antiguo soldado")
    num_misiones = fields.Integer(string="Número de misiones")
    en_reserva = fields.Boolean(string='En Reserva', compute='_compute_en_reserva', store=True)
    fecha_entrada_reserva = fields.Date(string="Fecha de entrada en reserva")
    turco_id = fields.Many2one(comodel_name='finalfantasy.turco', inverse_name='avalancha_id', string="Turco")

    @api.constrains('num_misiones')
    def _check_num_misiones(self):
          for record in self:
                if record.num_misiones >= 101:
                    raise models.ValidationError('Un miembro de Avalancha no puede tener más de 100 misiones realizadas.')

    @api.depends('num_misiones')
    def _compute_en_reserva(self):
        for record in self:
            if record.num_misiones >= 100:
                record.en_reserva = True
                record.fecha_entrada_reserva = fields.Date.today()
            else:
                record.en_reserva = False
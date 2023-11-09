from odoo import api, models, fields

class Moneda(models.Model):
    _name = 'durhos.moneda'
    cod_moneda = fields.Char( string="codigo", required=True)
    valor_facial = fields.Float(string="valor facial",required=True)
    unidad_monetaria = fields.Selection([
        ('pesetas', 'Pesetas'),
        ('euros', 'Euros'),
        ('otras', 'Otras')
    ], string='Unidad Monetaria', required=True)
    diametro = fields.Float(string="diametro (mm)")
    peso = fields.Float(string="peso (gr)")
    descripcion = fields.Char(string="descripcion")
    metal_ids = fields.One2many(comodel_name ='durhos.metal', inverse_name ='moneda_id')
    molde_ids = fields.One2many(comodel_name = 'durhos.molde', inverse_name = 'moneda_id')
    estado_id = fields.One2one(comodel_name = 'durhos.estado_conservacion', inverse_name="moneda_id")
    
class Metal(models.Model):
    _name = 'durhos.metal'
    proporcion = fields.Float(string="proporcion %")
    ley = fields.Char(string = "ley")
    moneda_id = fields.Many2one(comodel_name ='durhos.moneda', inverse_name ='metal_ids')
    
class Molde(models.Model):
    _name = 'durhos.molde'
    _description = 'Molde para la acuñación de monedas'
    cod_molde = fields.Char( string="molde", required=True)
    año_acuñacion = fields.Date( required=True)
    año_visible = fields.Char(string="año visible del molde")
    estrella_id = fields.One2many(comodel_name = 'durhos.estrella', inverse_name='molde_id')
    moneda_id = fields.Many2one (comodel_name = "durhos.moneda", inverse_name ='molde_id')
    
class Estrella(models.Model):
    _name = 'durhos.estrella'
    _description = 'Estrellas grabadas en el molde'
    fecha_grabada = fields.Date(string="")
    molde_id = fields.Many2one(comodel_name = 'durhos.molde', inverse_name='estrella_id')
    
class Estado_Conservacion(models.Model):
    _name = 'durhos.estado_conservacion'
    precio = fields.Float()
    estado = fields.Selection([
        ('BC', 'MBC'),
        ('EBC', 'SC'),
        
    ], string='Estado', required=True)
    nombre = fields.Char()
    descripcion = fields.Char()
    moneda_id = fields.One2one (comodel = "durhos.moneda", inverse_name="estado_id")
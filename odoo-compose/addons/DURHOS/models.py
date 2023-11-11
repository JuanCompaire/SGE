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
    estado_moneda_id = fields.Many2one(comodel_name='durhos.estado_moneda', inverse_name='moneda_id') 
    
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
    
class Estado_moneda(models.Model):
    _name = 'durhos.estado_moneda'
    precio = fields.Float()
    estado = fields.Selection([
        ('BC', 'MBC'),
        ('EBC', 'SC'),
        
    ], string='Estado', required=True)
    nombre = fields.Char()
    descripcion = fields.Char()
    moneda_id = fields.One2many(comodel_name = 'durhos.moneda', inverse_name='estado_moneda_id')


class Ejemplar(models.Model):
    _name = 'durhos.ejemplar'
    cod_ejemplar = fields.Char(string="codigo", required=True)
    num_correlativo = fields.Char(string="numero correlativo", required=True)
    precio = fields.Float(string="precio")
    fecha_adquisicion = fields.Date(string="fecha de adquisicion")
    proveedor_id = fields.Many2many(comodel_name='durhos.proveedor', inverse_name='ejemplar_id')
    cliente_id = fields.Many2one(comodel_name='durhos.cliente', inverse_name='ejemplar_id')
    estado_conservacion_ejemplar_id = fields.Many2one(comodel_name='durhos.estado_ejemplar', inverse_name='ejemplar_id')

class Proveedor(models.Model):
    _name = 'durhos.proveedor'
    _description = 'Proveedores que pueden adquirir monedas'
    nombre = fields.Char(string="nombre", required=True)
    direccion = fields.Char(string="direccion", required=True)
    telefono = fields.Char(string="telefono", required=True)
    ejemplar_id = fields.Many2many(comodel_name='durhos.ejemplar', inverse_name='proveedor_id')

class Cliente(models.Model):
    _name = 'durhos.cliente'
    _description = 'Clientes que pueden adquirir monedas'
    fecha = fields.Date(string="fecha", required=True)
    precio_venta = fields.Float(string="precio de venta", required=True)
    nombre_cliente = fields.Char(string="nombre del cliente", required=True)
    telefono = fields.Char(string="telefono", required=True)
    num_compras_realizadas = fields.Integer(string="numero de compras realizadas", required=True)
    ejemplar_id = fields.One2many(comodel_name='durhos.ejemplar', inverse_name='cliente_id')    

class Estado_ejemplar(models.Model):
    _name = 'durhos.estado_ejemplar'
    ajuste = fields.Selection([
        ('+', '-'),
    ], string='Unidad Monetaria', required=True)
    comentario = fields.Char(string="comentario")
    ejemplar_id = fields.One2many(comodel_name='durhos.ejemplar', inverse_name='estado_conservacion_ejemplar_id')
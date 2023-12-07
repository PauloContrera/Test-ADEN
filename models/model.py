from odoo import models, fields

class Alumno(models.Model):
    _name = 'colegio.alumno'
    _description = 'Alumno'

    nombre = fields.Char()
    apellido = fields.Char()
    fecha_nacimiento = fields.Date()
    legajo = fields.Integer()
    email = fields.Char()
    telefono = fields.Char()
    direccion = fields.Char()
    pais_id = fields.Many2one('res.country', string='País')

class Programa(models.Model):
    _name = 'colegio.programa'
    _description = 'Programa'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')


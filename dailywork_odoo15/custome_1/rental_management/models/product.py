from odoo import models, fields, api


class rental_management(models.Model):
    _name = 'product.detail'
    _description = 'product.details'

    name = fields.Char()
    quantity = fields.Integer()
    quality = fields.Integer()


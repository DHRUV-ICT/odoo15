from odoo import models, fields, api


class Rental_Management(models.Model):

    _name = 'rental.management'
    _description='rental.management'

    name_re = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    price = fields.Float()
    sale = fields.Float()

    customer = fields.Many2one('res.partner')
    # rental_type=fields.Many2one()
    rental_product = fields.Many2one('product.product')

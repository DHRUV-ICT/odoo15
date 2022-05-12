from odoo import models, fields, api



class shop(models.Model):

    _name = 'shop.shop'

    cart = fields.Many2many('data.data',compute='m2m')
    details = fields.One2many('data.data','total')

    @api.depends('cart')
    def m2m(self):
        ids = [15,16,17]
        self.write({'cart':[(6,0,ids)]})
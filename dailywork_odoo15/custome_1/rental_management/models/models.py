# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rental_management(models.Model):
    _name = 'rental_management.rental_management'
    _description = 'rental_management.rental_management'


    name = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    price = fields.Float()
    state = fields.Selection([('1', 'gujrat'), ('2', 'maharastra'), ('3', 'chennai')])

    customer = fields.Many2one('res.partner')
    rental_type = fields.Many2one('rental_management_menu2.rental_management_menu2', string="product_type")
    rental_product = fields.Many2one('product.product')


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rental_management_2(models.Model):
    _name = 'rental_management_2.rental_management_2'
    _description = 'rental_management_2.rental_management_2'

    name = fields.Char()
    start_date=fields.Date()
    end_date=fields.Date()
    price=fields.Float()
    sale=fields.Float()

    customer=fields.Many2one('res.partner')
    #rental_type=fields.Many2one()
    rental_product=fields.Many2one('product.product')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

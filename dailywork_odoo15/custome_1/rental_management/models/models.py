# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rental_management(models.Model):
    _name = 'rental_management.rental_management'
    _description = 'rental_management.rental_management'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    """manny 2 manny product.detail"""
    products = fields.Many2many('product.detail',compute="_products")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.depends('name')
    def _products(self):
        ids = [2,1]
        self.write({"products":[(6,0,ids)]})
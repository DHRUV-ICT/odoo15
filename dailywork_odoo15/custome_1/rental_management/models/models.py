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

    """many2one product.detail"""
    product_m2o = fields.Many2one('product.detail')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.depends('name')
    def _products(self):
        ids = [2,1]
        self.write({"products":[(2),(1)]})

    # @api.depends('value')
    # def search_get(self):
    #     rec = self.env['rental_management.rental_management'].search([('value', '!=', False)]).read(['value'])
    #     rec1 = self.env['rental_management.rental_management'].browse()
    #     rec2 = self.env['rental_management.rental_management'].search_read([('value', '!=', False)])

    # print("##############%%%%%%%%%%%%%^^^^^^^^^^^^^^",rec)
    # print("##############%%%%%%%%%%%%%^^^^^^^^^^^^^^")
    # print(rec1)
    # print("##############%%%%%%%%%%%%%^^^^^^^^^^^^^^")
    # print(rec2)

    def search_get(self):
        rec = self.env['res.partner'].search([('email', '!=', False)]).read(['email'])
        rec1 = self.env['res.partner'].browse()
        rec2 = self.env['res.partner'].search_read([('email', '!=', False)])

        print("##############%%%%%%%%%%%%%^^^^^^^^^^^^^^")
        print(rec1)



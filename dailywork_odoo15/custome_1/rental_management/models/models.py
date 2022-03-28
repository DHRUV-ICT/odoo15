# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rental_management(models.Model):
    _name = 'rental_management.rental_management'
    _description = 'rental_management.rental_management'


    name = fields.Char()
    name_of_product = fields.Many2one('product.detail')
    quantity_of_product = fields.Integer()

    """manny 2 manny product.detail"""
    products = fields.Many2many('product.detail',compute="_products")



    @api.depends('name')
    def _products(self):
        ids = [2,1,4]
        self.write({"products":[(6,0,ids)]})

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

    # def search_get(self):
    #     rec = self.env['res.partner'].search([('email', '!=', False)]).read(['email'])
    #     rec1 = self.env['res.partner'].browse()
    #     rec2 = self.env['res.partner'].search_read([('email', '!=', False)])
    #
    #     print("##############%%%%%%%%%%%%%^^^^^^^^^^^^^^")
    #     print(rec1)
    #

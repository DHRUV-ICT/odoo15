# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rental_management(models.Model):


    _name = 'wiza.wiza'
    _description = 'wiza.data'
    _rec_name = 'customer'

    customer = fields.Many2one('sale.order')
    email = fields.Char()
    sales_person = fields.Char()
    sales_person_contact = fields.Integer()
    payment_terms = fields.Selection([('1','15 days'),('2','30days'),('3','deliever_recieved')])


# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wiza_wizard(models.TransientModel):
    _name = 'wiza.wizard'
    # _description = 'wiza.wiza'

    name = fields.Char(string="name")
    value = fields.Integer(string="amount")
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    wiza = fields.Integer()
    email = fields.Char(string='Email')
    abool = fields.Boolean()
    selection = fields.Selection([('a','A'),('b','B'),('c','C')])
    abin = fields.Binary()
    date = fields.Datetime()

# class b(models.Model):
#     _inherit = 'wiza.wiza'

    # gender = fields.Selection([('a','A'),('b','B')])

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


    def check(self):
        print("dhruv")
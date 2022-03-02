# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wiza(models.Model):
    _name = 'wiza.wiza'
    _description = 'wiza.wiza'
    _inherit = ['mail.thread', 'mail.activity.mixin']

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
    smart_button = fields.Integer()

class b(models.Model):
    _inherit = 'wiza.wiza'

    gender = fields.Selection([('a','A'),('b','B')])

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100



    def action_open_related_taxes(self):
        print("it is for smart button")


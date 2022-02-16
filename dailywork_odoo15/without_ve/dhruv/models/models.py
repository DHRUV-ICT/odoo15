# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dhruv(models.Model):
    _name = 'dhruv.dhruv'
    _description = 'dhruv.dhruv'

    name = fields.Char(string="name")
    value = fields.Integer(string="amount")
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    dhruv = fields.Integer()
    email = fields.Char(string='Email')
    abool = fields.Boolean()
    selection = fields.Selection([('a','A'),('b','B'),('c','C')])
    abin = fields.Binary()
    date = fields.Datetime()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100



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
    partner_id = fields.Many2one('res.partner')
    city = fields.Char(related="partner_id.city",readonly=False)

    state = fields.Many2one(related="partner_id.state_id",readonly=True)


class b(models.Model):
    _inherit = 'dhruv.dhruv'

    gender = fields.Selection([('a','A'),('b','B')])

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100



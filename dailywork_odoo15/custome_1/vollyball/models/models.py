# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vollyball(models.Model):
    _name = 'vollyball.vollyball'
    _description = 'vollyball.vollyball'

    name = fields.Char()
    sport_name = fields.Char()
    position= fields.Char()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

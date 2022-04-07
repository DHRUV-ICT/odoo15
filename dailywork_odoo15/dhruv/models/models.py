# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from datetime import date

class dhruv(models.Model):
    _name = 'dhruv.dhruv'
    _description = 'dhruv.dhruv'

    name = fields.Char('Name', default='New')
    value = fields.Integer(string="amount")
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    dhruv = fields.Integer()
    email = fields.Char(string='Email')
    abool = fields.Boolean()
    selection = fields.Selection([('a','A'),('b','B'),('c','C')])
    abin = fields.Binary()
    date = fields.Datetime()


    m2m = fields.Many2many('dhruv.one',string="manny_2_manny")
    many_2_one = fields.Many2one('res.partner')


    take = fields.Char(compute="_depend_value",store=True)
    # date = fields.Date('Date',default=lambda self: fields.datetime.now())


    # one 2 many
    one_2_manny = fields.One2many('dhruv.one','partner_id',string='one_2_manny')
    # partner_id_1 = fields.Many2one('res.partner')

    @api.depends('name')
    def _depend_value(self):
        for record in self:
            record.take = (record.name)


class one_2_manny(models.Model):
    _name = 'dhruv.one'

    partner_id = fields.Many2one('dhruv.dhruv')
    email_o2m= fields.Char(related="partner_id.email", readonly=False)
    date_o2m= fields.Datetime(related="partner_id.date", readonly=False)
    name_o2m = fields.Char(related="partner_id.name",readonly=False)
    value_o2m = fields.Integer(related="partner_id.value",readonly=False)
    abool_o2m = fields.Boolean(related="partner_id.abool",readonly=False)

    # m2m = fields.Many2many('dhruv.dhruv',string="manny_2_manny")


# class many_2_many(models.Model):

    # _inherit = 'dhruv.dhruv'

    # m2m = fields.Many2many('dhruv.dhruv')


    @api.depends('name')
    def _depend_value(self):
        for record in self:
            record.take = (record.name)


    #many2one build model
# class dhruv(models.Model):
#     _name = 'dhruv_m2o.dhruv_m2o'


# class b(models.Model):
#     _inherit = 'dhruv.dhruv'
#
#     gender = fields.Selection([('a','A'),('b','B')])
#
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100





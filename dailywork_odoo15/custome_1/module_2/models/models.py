# -*- coding: utf-8 -*-

from odoo import models, fields, api


class module_2(models.Model):
    _name = 'module_2.module_2'
    _description = 'module_2.module_2'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    selection = fields.Selection([('start','a'),('middle','b'),
                                  ('end','c')],
                                 string='dhruv',
                                 index=True,readonly=True,default="draft")


#this is for statusbar
class b(models.Model):
    _inherit = 'module_2.module_2'
    gender = fields.Char()




# class c(models.Model):
#     _name= 'module_2.module_2'  #it overwrite old function
#
#     name = fields.Integer()
#     girl = fields.Text()



@api.depends('value')
def _value_pc(self):
    for record in self:
        record.value2 = float(record.value) / 100

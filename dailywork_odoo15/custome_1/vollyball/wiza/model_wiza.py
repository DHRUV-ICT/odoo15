# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wizard(models.TransientModel):
    _name = 'wiza.wiza'
    _description = 'wiza.wiza'

    weight = fields.Integer()
    # position_wiza = fields.Integer()
    height = fields.Integer()

    def create_rec(self):
        # rtn = super(wizard,self).create(vals)
        rtn = self.env['related.related'].create({'height':self.height , 'weight':self.weight})
        return rtn

    def write_rec(self):
        rtn = self.env['related.related'].write({'height':self.height , 'weight':self.weight})
        return rtn

    # def write_rec(self):
    #
    #     rental_type = self.env['related.related'].browse(self.env.context.get("active_id"))
    #     rental_type.write({'height':self.height , 'weight':self.weight})
    #     # print(self.env['active_id'])

    def unlink_rec(self):
        rtn = self.env['related.related'].unlink(({'height': self.height}))
        return rtn

    # @api.depends('height')
    # def wiza_height(self):
    #     self.height = self.env['wiza.wiza'].browse(self.id).height


# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wizard(models.TransientModel):
    _name = 'wiza.wiza'
    _description = 'wiza.wiza'

    name = fields.Char()
    position_wiza = fields.Integer()

    @api.model
    def create(self,vals):
        rtn = super().create(vals)
        print(rtn)
        # rtn = self.env['related'].create(vals)
        return rtn

    def write(self,vals):
        rtn = super(wizard,self).write(vals)
        return rtn

    # def unlink(self,vals):
    #     rtn = super(self).unlink(vals)
    #     return rtn

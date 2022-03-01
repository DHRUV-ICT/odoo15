# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vollyball(models.Model):
    _name = 'vollyball.vollyball'
    _description = 'vollyball.vollyball'

    name = fields.Char()
    sport_name = fields.Char()
    position_number= fields.Integer()
    position = fields.Char(compute="position_name" , store=True)
    description = fields.Text()

    # @api.depends('position_number')
    # def position_name(self):
    #     for i in self:
    #         if i == 1:
    #             i.position= "libero"
    #             i.position= i.position_number

    @api.depends('position_number')
    def position_name(self):
        for record in self:
                if record.position_number == 1:
                    record.position = str("libero")
                elif record.position_number == 2:
                    record.position = str("universal")
                elif record.position_number == 3:
                    record.position = str("lifter")
                elif record.position_number == 4:
                    record.position = str("middle_blocker")
                elif record.position_number == 5:
                    record.position = str("outside_hitter")
                elif record.position_number == 6:
                    record.position = str("3 meter")

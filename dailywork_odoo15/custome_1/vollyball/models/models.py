# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vollyball(models.Model):
    _name = 'vollyball.vollyball'
    _description = 'vollyball.vollyball'
    position_number = fields.Integer()
    name = fields.Char(default="player name")
    sport_name = fields.Char()
    position = fields.Char(compute="position_name" , store=True)
    description = fields.Text()
    gender = fields.Selection([('male','male'),('female','female')])


    """this is many 2 one in main module but it has no logic"""
    #many 2 one
    # m2o_1 = fields.Many2one('vollyball.vollyball',string="m2o_1")
    # sport_name_m = fields.Char(realted='m2o_1.sport_name')
    # position_number_m = fields.Integer(realted='m2o_1.position_number')
    # position_m = fields.Char(realted='m2o_1.position')
    # description_m = fields.Text(realted='m2o_1.description')

    """one 2 manny"""
    o2m = fields.One2many('related.related','m2o',string='one_2_many')

    """manny 2 manny"""
    m2m = fields.Many2many('')
    '''this is ralation between two fields'''

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
                else:
                    record.position = str("no one or all rounder")


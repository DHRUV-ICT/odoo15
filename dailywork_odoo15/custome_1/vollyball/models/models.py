# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vollyball(models.Model):
    _name = 'vollyball.vollyball'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    """ for show speciality not object"""

    _rec_name = 'international_player'
    _description = 'vollyball.vollyball'

    position_number = fields.Integer(tracking=True)
    name = fields.Char(default="player name",tracking=True)
    sport_name = fields.Char(tracking=True)
    position = fields.Char(compute="position_name" , store=True,tracking=True)
    description = fields.Text(tracking=True)
    gender = fields.Selection([('male','male'),('female','female')],tracking=True)
    spiker = fields.Boolean(tracking=True)

    """this is status bar """
    status = fields.Selection([('a','player_name'),('b','info'),('c',"world's player")]
                              ,string='status',default='a',tracking=True)

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
    # m2m = fields.Many2many('player.player',string='wwp')
    player_id = fields.Many2many('player.player')
    international_player = fields.Char(related='player_id.famous_player_name',string="world's player")
    # task = fields.Many2one('player.player',string="task")


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

    # @api.depends('position_number')
    # def famous_player(self):
    #     for record in self:
    #         if record.position_number == 1 :
    #             for x in record.m2m.speciality():
    #                 if x == 'libero':
    #                     record.players_famous = record.m2m.famous_player_name




    @api.depends('player_name')
    def player_name(self):
        self.status='a'

    def info(self):
        self.status='b'

    def international(self):
        self.status = 'c'

    """this is orm methods create"""

    # @api.model
    # def create(self, vals):
    #     rtn = super(vollyball, self).create(vals)
    #     # rtn = self.env['related'].create(vals)
    #     return rtn
    #
    # def write(self,vals):
    #     # vals.update({'name':'toru'})
    #     rtn = super(vollyball,self).write(vals)
    #     return rtn




    # @api.model_create_multi
    # def create(self,values):
    #     res = super(vollyball,self).create(values)
    #
    #     print('before',values)
    #     # values['spiker']=True
    #     print('after',values)
    #
    #     return res

    # @api.model_create_multi
    # def create(self, vals_list):
    #     print("CREATEEEEEEEEEEE", vals_list)
    #     res = super(vollyball,self).create(vals_list)
    #     print("resresres", res)
    #     return res




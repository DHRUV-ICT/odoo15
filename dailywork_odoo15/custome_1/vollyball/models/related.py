from odoo import models, fields, api

class related(models.Model):
    """manny 2 one class"""

    _inherit='vollyball.vollyball'
    _name = 'related.related'
    _description = 'related.related'


    """ manny 2 one field"""
    m2o = fields.Many2one('vollyball.vollyball',string='manny_2_one')

    height = fields.Integer()
    weight =  fields.Integer()

    sport_name_m = fields.Char(related="m2o.sport_name")
    position_number_m = fields.Integer(related="m2o.position_number")
    position_m = fields.Char(related="m2o.position")



class data(models.Model):
    """this is for extra practice"""

    _name = 'player.player'

    player

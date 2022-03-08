from odoo import models, fields, api


class related(models.Model):
 """manny 2 one class"""

 _name = 'player.player'
 _description = 'player.player'

 famous_player_name =fields.Char()
 speciality = fields.Char()


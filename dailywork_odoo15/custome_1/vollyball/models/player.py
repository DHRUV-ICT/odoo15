from odoo import models, fields, api


class related(models.Model):
    """manny 2 one class"""

    _name = 'player.player'
    _rec_name = 'famous_player_name'

    _description = 'player.player'

    famous_player_name = fields.Char()
    speciality = fields.Char()


    # @api.model
    # def create(self, vals):
    #  rtn = super(related, self).create(vals)
    #  # rtn = self.env['related'].create(vals)
    #  return rtn
    #
    # def write(self, vals):
    #  vals.update({'name':'orm'})
    #  rtn = super(related, self).write(vals)
    #  # rtn = self.env['related'].create(vals)
    #  return rtn

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.famous_player_name, rec.speciality)))
            print(result)
        return result
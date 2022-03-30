from odoo import models, fields, api


class res(models.Model):

    _inherit = 'res.partner'

    def change_value(self):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        self.update({'name':'ABCD'})
        self.update({'email':'ABCD'})
        self.update({'mobile':'ABCD'})
        # rec1 = self.env['res.partner'].update({'name':'ABCD'})
        # return  rec1

from odoo import models, fields, api
from ast import literal_eval
from datetime import date, datetime


class ResConfiSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    module_exam_2 = fields.Boolean(string="install")
    pro_items = fields.Many2many('sale.order', domain=[("date_order", '>=', datetime(date.today().year, date.today().month, 1))])

    @api.model
    def get_values(self):
        res = super(ResConfiSetting, self).get_values()
        Values = self.env['ir.config_parameter']

        pro_items = Values.get_param('Exam_2.pro_items')
        lines = False
        if pro_items:
            lines = [(6, 0, literal_eval(pro_items))]
        return {
            'pro_items': lines,

        }

    @api.model
    def set_values(self):
        res = super(ResConfiSetting, self).set_values()
        print(self.pro_items.ids, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
        self.env['ir.config_parameter'].set_param(
            'Exam_2.pro_items', self.pro_items.ids)
        return res



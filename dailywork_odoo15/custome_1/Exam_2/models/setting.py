from odoo import models, fields, api
from ast import literal_eval
from datetime import date, datetime


class ResConfiSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    module_Exam_2 = fields.Boolean(string="install")
    product_ids = fields.Many2many('sale.order', string="Sale Data",
                                   domain=[("date_order", '>=', datetime(date.today().year, date.today().month, 1))])

    @api.model
    def get_values(self):
        res = super(ResConfiSetting, self).get_values()
        Values = self.env['ir.config_parameter']
        # module_Exam_2 = Values.get_param('Exam_2.module_Exam_2')
        product_ids = Values.get_param('Exam_2.product_ids')
        lines = False
        if product_ids:
            lines = [(6, 0, literal_eval(product_ids))]
        return {
            'product_ids': lines,
            # 'module_Exam_2': module_Exam_2,
        }

    @api.model
    def set_values(self):
        res = super(ResConfiSetting, self).set_values()
        print(self.product_ids.ids, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
        # self.env['ir.config_parameter'].set_param(
        # 'Exam2.module_Exam_2', self.module_Exam_2)
        self.env['ir.config_parameter'].set_param(
            'Exam_2.product_ids', self.product_ids.ids)
        return res



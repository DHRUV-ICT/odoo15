# from odoo import models, fields, api
# from odoo.exceptions import UserError
#
# class temp(models.Model):
#     _inherit = 'sale.order'
#
#
#     age = fields.Char()
#     b_date = fields.Date()
#
#
#
#     def action_confirm(self):
#         for rec in self:
#             count = len(rec.order_line)
#             if count > 3:
#                 raise UserError('UserError: You can only add max 3 lines per order')
#             else:
#                 return super(temp,self).action_confirm()
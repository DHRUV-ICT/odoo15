# from odoo import models, fields, api
#
# class sale_inhe(models.Model):
#
#     _inherit = 'sale.order'
#
#
#     """name_get"""
#     def name_get(self):
#         result = []
#         for rec in self:
#             result.append((rec.id, '%s , %s' % (rec.name,rec.client_order_ref)))
#             print(result)
#         return result
#

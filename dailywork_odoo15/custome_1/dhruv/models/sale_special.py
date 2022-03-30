from odoo import models, fields, api

class special(models.Model):
    _inherit = 'sale.order'

    # @api.model
    # def create(self,values):
    #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #     rec = super(special,self).create(values)
    #
    #     if rec.partner_id.customer_rank > 5:
    #         rec.partner_id.write({'category_id':[(4,8)]})
    #
    #     return rec

    @api.model
    def create(self, vals):
        res = super(special, self).create(vals)
        if res.partner_id.customer_rank > 5:

            res.partner_id.write({'category_id': [(4, 8)]})  # 4 - Link, 8 - id of Best Customer tag
        return res

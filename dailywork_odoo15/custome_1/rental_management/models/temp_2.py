from odoo import models, fields, api
from datetime import date

class temp_2(models.Model):
    _inherit = 'sale.order'

    email = fields.Char()
    Mobile = fields.Char()
    customer_ref = fields.Char()

    age = fields.Date(compute='your_age')
    b_date = fields.Date()
    # today_date = fields.Date(default=date.today())
    from_date = fields.Date(string="From Date", default=date.today())

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            rec.email = rec.partner_id.email
            rec.Mobile = rec.partner_id.phone


    @api.constrains('partner_id','payment_term_id')
    def _payment_com(self):
        for rec in self:
            if rec.payment_term_id != rec.partner_id.property_supplier_payment_term_id:
                raise ('payment term do not match')

    # def _name_get(self):
    #     result=[]
    #     for rec in self:
    #             result.append((rec.id, '%s - %s' % (rec.partner_id, rec.phone)))
    #             print(result)
    #     return result

    @api.depends('client_order_ref')
    def ref(self):
        for rec in self:
            res = super('sale.order', self).default_get(fields)
            rec.customer_ref = res.client_order_ref


    @api.depends('b_date','from_date')
    def your_age(self):
        if self.from_date > self.b_date:
            raise ('afafafafaf')



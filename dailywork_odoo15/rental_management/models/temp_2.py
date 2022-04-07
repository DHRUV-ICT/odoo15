from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError

class temp_2(models.Model):
    _inherit = 'sale.order'

    email = fields.Char()
    Mobile = fields.Char()
    customer_ref = fields.Char()

    age = fields.Integer(compute='_compute_your_age')
    b_date = fields.Date()
    from_date = fields.Date(string="From Date", default=date.today())

    read_rec = fields.Char()

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
    def _compute_your_age(self):
        if self.b_date:
            self.age = self.from_date.year - self.b_date.year
        else:
            self.age = 0


    """read search_read browsw"""

    # @api.depends('email')
    def search_get(self):
        rec = self.env['res.partner'].search([('email','!=',False)]).read(['email'])
        rec1 = self.env['res.partner'].browse()
        rec2 = self.env['res.partner'].search_read([('email','!=',False)])

        print("##############%%%%%%%%%%%%%^^^^^^^^^^^^^^")
        print(rec1)
        # if self.read_rec:
        #     self.read_rec  = rec
        # return rec , rec1 , rec2


    def action_confirm(self):
        for rec in self:
            count = len(rec.order_line)
            if count > 3:
                raise UserError('UserError: You can only add max 3 lines per order')
            else:
                return super(temp_2,self).action_confirm()
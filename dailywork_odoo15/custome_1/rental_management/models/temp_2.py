from odoo import models, fields, api


class temp_2(models.Model):
    _inherit = 'sale.order'

    email = fields.Char()
    Mobile = fields.Char()
    customer_ref = fields.Char()

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


    def any(self):
        print("hyyyy uyk ifguloioi;ojio;i9p0lki985tadfnaskfvgay7uaakusvfkasvfa ")


    def _name_get(self):
        result=[]
        for rec in self:
                result.append((rec.id, '%s - %s' % (rec.date_order, rec.payment_term_id)))
                print(result)
        return result

    @api.depends('client_order_ref')
    def ref(self):
        for rec in self:
            res = super(temp_2, self).default_get(fields)
            rec.customer_ref = res.client_order_ref

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rental_management_wiza(models.Model):


    _name = 'wiza.wiza'
    _description = 'wiza.data'
    _rec_name = 'customer'


    customer = fields.Char()
    email = fields.Char()
    sales_person = fields.Char()
    sales_person_contact = fields.Char()
    payment_term = fields.Char()
    # payment_terms = fields.Selection([('1','15 days'),('2','30days'),('3','deliever_recieved')])


    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, '%s - %s' % (rec.partner_id.name, rec.partner_id.email)))
    #         print(result)
    #     return result

    @api.model
    def default_get(self, fields):
        vals = super(rental_management_wiza, self).default_get(fields)
        res = self.env['sale.order'].browse([self.env.context.get('active_id')])
        vals.update({
            'customer': res.partner_id.name,
            'email': res.email,
            'sales_person': res.user_id.name,
            'sales_person_contact': res.user_id.phone,
            'payment_term': res.payment_term_id.name,
        })
        return vals
    #
    # def name_search(self, name='', args=None, operator='=', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', ('phone', operator, name), ('email', operator, name)]
    #     return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

from odoo import models, fields, api


class product_detail(models.Model):
    _name = 'product.detail'
    _description = 'product.details'

    name = fields.Char()
    quantity = fields.Integer()
    quality = fields.Integer()

    """name_get"""
    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f"{rec.name} ,  {rec.quantity}"))
            print(result)
        return result
    """name search"""
    def _name_search(self, name='', args=None, operator='=', limit=100, name_get_uid=None):
        args = args or []
        domain = ['|','|', ('quantity', operator, name), ('quality', operator, name),('name', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
    """default get"""
    def default_get(self, fields):
        res = super(product_detail, self).default_get(fields)
        print('test.....')
        res['name'] = 'aaa'
        return res


    """on change """
    @api.model
    def stock(self,fields):
        vals = super(product_detail,self).write(fields)
        res = self.env['rental_management.rental_management'].browse([self.env.context.get('active_id')])

        vals.update({self.quantity : self.quantity - res.rental_management.quantity_of_product})

        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',res)

        return vals


    # @api.model
    # def default_get(self, fields):
    #     vals = super(rental_management_wiza, self).default_get(fields)
    #     res = self.env['sale.order'].browse([self.env.context.get('active_id')])
    #     vals.update({
    #         'customer': res.partner_id.name,
    #         'email': res.email,
    #         'sales_person': res.user_id.name,
    #         'sales_person_contact': res.user_id.phone,
    #         'payment_term': res.payment_term_id.name,
    #     })
    #     return vals


from odoo import models, fields, api


class rental_management(models.Model):
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
        res = super(rental_management, self).default_get(fields)
        print('test.....')
        res['name'] = 'aaa'
        return res



from odoo import models, fields, api

class sale_inhe(models.Model):
    _inherit = 'res.partner'



    """name_get"""
    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.name, rec.phone)))
            print(result)
        return result


    """name_search"""

    @api.model
    def _name_search(self, name='', args=None, operator='=', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('email', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    """NAME SEARCH"""

    # def name_search(self, name='', args=None , operator='',limit=100 , nmae_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|',('name', operator , name),('phone',operator,email)]
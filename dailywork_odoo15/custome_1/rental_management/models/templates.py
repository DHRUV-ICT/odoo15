from odoo import models, fields, api


class templates(models.Model):
    _inherit = 'product.template'
    # _name = 'templates.templates'

    is_rental = fields.Boolean()
    rental_type_id = fields.Many2one('rental_management_menu2.rental_management_menu2')

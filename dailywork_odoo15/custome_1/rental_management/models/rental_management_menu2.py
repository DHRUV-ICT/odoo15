from odoo import models, fields, api


class rental_management_menu2(models.Model):
    _name = 'rental_management_menu2.rental_management_menu2'
    _description = 'rental_management_menu2.rental_management_menu2'

    Name = fields.Char()
    Code = fields.Char()
    Description = fields.Char()

    is_rental = fields.Boolean()
    rental_type_2 = fields.Many2one('rental_management_menu2.rental_management_menu2')

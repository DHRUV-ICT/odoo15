from odoo import models, fields, api


class templates(models.Model):
    _inherit = 'product.template'
    # _name = 'templates.templates'

    is_rental = fields.Boolean()
    rental_type_id = fields.Many2one('rental_management_menu2.rental_management_menu2')



    # @api.onchange('partner_id')
    # def onchange_partner_id(self):
    #     for rec in self:
    #         if rec.partner_id:
    #             rec.
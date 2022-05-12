from odoo import models, fields, api


class invoice_add(models.Model):
    _inherit = 'account.move.line'

    delivery_add = fields.Many2one('res.partner')
    vendor = fields.Many2one('res.partner',
                             domain=[("supplier_rank", '>', 0)])

    vendor_price = fields.Float()
    planned_gp = fields.Float(compute='calculate_planned_gp')
    description = fields.Text(compute='_description_data')

    def calculate_planned_gp(self):
        for rec in self:
            if rec.vendor_price:
                rec.planned_gp = ((rec.price_unit - rec.vendor_price)/rec.price_unit)*100
            else:
                rec.planned_gp = 0

    @api.depends("delivery_add", "product_id.description")
    def _description_data(self):
        for rec in self:
            rec.description = f"{rec.product_id and rec.product_id.description or 'null'} {rec.delivery_add and rec.delivery_add.name or 'null' }"


































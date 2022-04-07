from odoo import models, fields, api


class exam_wizard(models.TransientModel):
    _name = 'exam.wiz'
    _description = 'exam_wizard'

    order_line = fields.One2many('exam.o2m', 'relation_o2m', string="Order Line")


class o2m(models.TransientModel):
    _name = 'exam.o2m'
    _description = 'exam_o2m'

    relation_o2m = fields.Many2one('exam.wiz', string="Relation")
    product = fields.Many2many('product.product', string="Product")
    quantity = fields.Float(string="QTY")
    unit_price = fields.Float(string="Unit Price")

from odoo import models, fields, api


class wiza_exam(models.TransientModel):
    _name = 'exam_wizard'
    _description = 'exam_wizard'

    o2m_fi = fields.One2many('exam_one2manny', 'relation_fi', string="Order Line")


class o2m(models.TransientModel):
    _name = 'exam_one2manny'
    _description = 'exam_one2manny'

    relation_fi = fields.Many2one('exam.wizard', string="Relation")
    product = fields.Many2many('product.product', string="Product")
    quantity = fields.Float(string="QTY")
    unit_price = fields.Float(string="Unit Price")






























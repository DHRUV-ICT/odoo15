from odoo import models, fields, api


class wiza_exam(models.TransientModel):
    _name = 'exam.wizard'
    _description = 'exam_wizard'

    o2m_fi = fields.One2many('exam.one2manny', 'relation_fi', string="Order Line")



    def so_create(self):
        print('D########$$$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%')
        orders = []
        for product in self.o2m_fi.product:
            orders.append((0, 0, {'product_id': product.id}))
        for i in self._context.get("active_ids"):
            self.env['sale.order'].create({
                'partner_id': i,
                'order_line': orders
            })
        # return self.env['ir.actions.act_window']._for_xml_id("sale.action_quotations_with_onboarding")


class o2m(models.TransientModel):
    _name = 'exam.one2manny'
    _description = 'exam_one2manny'

    relation_fi = fields.Many2one('exam.wizard', string="Relation")
    product = fields.Many2one('product.product', string="Product")
    quantity = fields.Float(string="QTY", default=1)
    unit_price = fields.Float(string="Unit Price")

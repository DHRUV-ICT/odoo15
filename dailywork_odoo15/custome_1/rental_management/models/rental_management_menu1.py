from odoo import models, fields, api

class rental_management_menu1(models.Model):

    _name = 'rental_management_menu1.rental_management_menu1'
    _description='rental_management_menu1.rental_management_menu1'
    # _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(required="True")
    start_date = fields.Date()
    price = fields.Float(required="True")
    state = fields.Selection([('1','gujrat'),('2','maharastra'),('3','chennai')])
    end_date = fields.Date()


    customer = fields.Many2one('res.partner')
    rental_type = fields.Many2one('rental_management_menu2.rental_management_menu2',string="m_2_o")
    rental_product = fields.Many2one('product.product')

    status = fields.Selection([('a','draft'),('b','waiting'),('c','approve'),('d','ncle')],
                              string='status',
                              default='a')


    @api.constrains('start_date','end_date')
    def datechange(self):
        if (self.start_date)>(self.end_date):
            raise 'start date is greater than end date'




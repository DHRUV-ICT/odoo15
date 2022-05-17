from odoo import models, fields, api

class data(models.Model):

    _name = 'data.data'

    book = fields.Many2one('libary.libary')
    price = fields.Float()
    author = fields.Char()
    total = fields.Integer()
    type = fields.Selection([('0','love_story'),('1','history'),
                            ('2','motivational'),('3','drama'),])

    @api.onchange('book')
    def onchange_price(self):
        if self.book:
            if self.book.price:
                self.price = self.book.price
                print('yaaaa onvahnge is runningggggg')

            if self.book.author:
                self.author = self.book.author

            if self.price:
                self.total = self.price


    @api.onchange('type')
    def onchange_type(self):
        if self.type:
            domain = {'book':[('genre','=',self.type)]}
            return {'domain':domain}
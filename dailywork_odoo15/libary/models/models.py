# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError




class libary(models.Model):

    _name = 'libary.libary'
    _description = 'libary.libary'
    _rec_name = 'book_name'
    _inherit = 'hr.contract'

    book_name = fields.Char()
    genre = fields.Selection([('0', 'love_story'), ('1', 'history'),
                             ('2', 'motivational'), ('3', 'drama'), ])
    review = fields.Selection(
        [('0', 'Bad'), ('1', 'Average'), ('2', 'Good'),
         ('3', 'very good'), ('4', 'Excellent'), ('5', 'Master')])

    book_id = fields.Integer(string='book_id')
    price = fields.Float()
    author = fields.Char()

    publisher = fields.Char()
    published_date = fields.Date()
    description = fields.Text()
    language = fields.Selection([('1', 'gujrati'), ('2', 'hindi'), ('3', 'english')])
    binding = fields.Selection([('1', 'paper'), ('2', 'spiral'), ('3', 'sewn'), ('4', 'Lay-flat')])
    photo = fields.Binary()
    email = fields.Char()




    # hyy = fields.Char()
    #
    # def email_books_order(self):
    #     template_id = self.env.ref("libary.dhruv_mail").id
    #     self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)


    @api.model
    def create(self,value):
        record = super(libary,self).create(value)
        record['email'] = 'ladoladhruv@gmail.com'
        print('succesfully add   #########$$$$$$$$$$$%%%%%%%%%%%',record)
        return record


    def write(self,values):
        record_w = super(libary,self).write(values)
        print('WWWWWRRRRR@@@@@@@@@@@##@@@@@@@@@@@#@@@@@  @@@@@@@@$@@@@@@@@@@@@@@')
        return record_w

    def unlink(self):
        record_d = super().unlink()
        print('deeeeleeetttt')
        return record_d


    # constrains for check
    # @api.constrains('book_name')
    # def name_check(self):
    #     for rec in self:
    #         same_name =  self.env['libary.libary'].search([('book_name','=', rec.book_name)])
    #         if same_name:
    #             raise ValidationError(('same name can not be accepted',rec.book_name))


    @api.constrains('price')
    def check_price(self):
        for rec in self:
            if rec.price == 0:
                raise ValidationError(('price must be aboove zero '))

    _sql_constraints = [ ('book_name', 'unique(book_name)' , 'book name must not be same')]

    def upload_file(self):
        pass
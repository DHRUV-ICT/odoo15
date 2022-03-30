# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libary(models.Model):
    _name = 'libary.libary'
    _description = 'libary.libary'

    book_name = fields.Char()
    genre = fields.Char()
    review = fields.Selection(
        [('0', 'Bad'), ('1', 'Average'), ('2', 'Good'),
         ('3', 'very good'), ('4', 'Excellent'), ('5', 'Master')])

    book_id = fields.Integer(string='book_id')
    price = fields.Float()
    author = fields.Char()

    publisher = fields.Char()
    published_date = fields.Date()
    description = fields.Text()
    language = fields.Selection([('1','gujrati'),('2','hindi'),('3','english')])
    binding = fields.Selection([('1','paper'),('2','spiral'),('3','sewn'),('4','Lay-flat')])
    photo = fields.Binary()
    # hyy = fields.Char()


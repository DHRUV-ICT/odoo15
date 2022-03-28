# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libary(models.Model):
    _name = 'libary.libary'
    _description = 'libary.libary'

    book_name = fields.Char()
    genre = fields.Char()
    author = fields.Char()
    description = fields.Text()
    book_id = fields.Integer(string='book_id')
    photo = fields.Binary()
    price = fields.Float()
    publisher = fields.Char()
    published_date = fields.Date()
    review = fields.Float()
    language = fields.Selection([('1','gujrati'),('2','hindi'),('3','english')])
    binding = fields.Selection([('1','paper'),('2','spiral'),('3','sewn'),('4','Lay-flat')])
    # hyy = fields.Char()

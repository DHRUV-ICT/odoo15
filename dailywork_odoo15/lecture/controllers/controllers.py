# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    @http.route(['/contacts'], type='http', auth="user", website=True)
    def contacts(self, **data):
        contacts = request.env['res.partner'].sudo().search([])
        return request.render(
            "lecture.contacts_list", {})


    @http.route(['/contacts/<model("res.partner"):con>'], auth='public', type='http', website=True)
    def display_contacts(self, con):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', con)
        return request.render('lecture.dis_contact', {
            'details': con,
        })

# class Lecture(http.Controller):
#     @http.route('/lecture/lecture', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lecture/lecture/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lecture.listing', {
#             'root': '/lecture/lecture',
#             'objects': http.request.env['lecture.lecture'].search([]),
#         })

#     @http.route('/lecture/lecture/objects/<model("lecture.lecture"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lecture.object', {
#             'object': obj
#         })

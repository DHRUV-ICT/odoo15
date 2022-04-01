# -*- coding: utf-8 -*-
# from odoo import http
# from odoo import http, _
# from odoo.http import request
#
# class Website(http.Controller):
#     @http.route(['/contacts'], type='http', auth="user", website=True)
#     def contacts(self, **data):
#         contacts = request.env['res.partner'].sudo().search([])
#         return request.render(
#             "dhruv.contacts_list", {})

# class Dhruv(http.Controller):
#     @http.route('/dhruv/dhruv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dhruv/dhruv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dhruv.listing', {
#             'root': '/dhruv/dhruv',
#             'objects': http.request.env['dhruv.dhruv'].search([]),
#         })

#     @http.route('/dhruv/dhruv/objects/<model("dhruv.dhruv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dhruv.object', {
#             'object': obj
#         })

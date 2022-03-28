# -*- coding: utf-8 -*-
# from odoo import http


# class Libary(http.Controller):
#     @http.route('/libary/libary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libary/libary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libary.listing', {
#             'root': '/libary/libary',
#             'objects': http.request.env['libary.libary'].search([]),
#         })

#     @http.route('/libary/libary/objects/<model("libary.libary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libary.object', {
#             'object': obj
#         })

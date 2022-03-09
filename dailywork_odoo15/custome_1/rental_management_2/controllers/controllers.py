# -*- coding: utf-8 -*-
# from odoo import http


# class RentalManagement2(http.Controller):
#     @http.route('/rental_management_2/rental_management_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rental_management_2/rental_management_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rental_management_2.listing', {
#             'root': '/rental_management_2/rental_management_2',
#             'objects': http.request.env['rental_management_2.rental_management_2'].search([]),
#         })

#     @http.route('/rental_management_2/rental_management_2/objects/<model("rental_management_2.rental_management_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rental_management_2.object', {
#             'object': obj
#         })

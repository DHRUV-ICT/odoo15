# -*- coding: utf-8 -*-
# from odoo import http


# class Pioneer(http.Controller):
#     @http.route('/pioneer/pioneer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pioneer/pioneer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pioneer.listing', {
#             'root': '/pioneer/pioneer',
#             'objects': http.request.env['pioneer.pioneer'].search([]),
#         })

#     @http.route('/pioneer/pioneer/objects/<model("pioneer.pioneer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pioneer.object', {
#             'object': obj
#         })

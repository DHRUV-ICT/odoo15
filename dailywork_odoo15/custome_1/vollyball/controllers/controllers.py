# -*- coding: utf-8 -*-
# from odoo import http


# class Vollyball(http.Controller):
#     @http.route('/vollyball/vollyball', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vollyball/vollyball/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vollyball.listing', {
#             'root': '/vollyball/vollyball',
#             'objects': http.request.env['vollyball.vollyball'].search([]),
#         })

#     @http.route('/vollyball/vollyball/objects/<model("vollyball.vollyball"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vollyball.object', {
#             'object': obj
#         })

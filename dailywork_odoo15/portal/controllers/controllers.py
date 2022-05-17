# -*- coding: utf-8 -*-
# from odoo import http


# class Portal(http.Controller):
#     @http.route('/portal/portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal/portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal.listing', {
#             'root': '/portal/portal',
#             'objects': http.request.env['portal.portal'].search([]),
#         })

#     @http.route('/portal/portal/objects/<model("portal.portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal.object', {
#             'object': obj
#         })

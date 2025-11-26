# -*- coding: utf-8 -*-
# from odoo import http


# class Rentsurf(http.Controller):
#     @http.route('/rentsurf/rentsurf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentsurf/rentsurf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentsurf.listing', {
#             'root': '/rentsurf/rentsurf',
#             'objects': http.request.env['rentsurf.rentsurf'].search([]),
#         })

#     @http.route('/rentsurf/rentsurf/objects/<model("rentsurf.rentsurf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentsurf.object', {
#             'object': obj
#         })


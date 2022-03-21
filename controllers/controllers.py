# -*- coding: utf-8 -*-
from odoo import http

# class Blackcats(http.Controller):
#     @http.route('/blackcats/blackcats/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blackcats/blackcats/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('blackcats.listing', {
#             'root': '/blackcats/blackcats',
#             'objects': http.request.env['blackcats.blackcats'].search([]),
#         })

#     @http.route('/blackcats/blackcats/objects/<model("blackcats.blackcats"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blackcats.object', {
#             'object': obj
#         })
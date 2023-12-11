# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo16(http.Controller):
#     @http.route('/odoo16/odoo16', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo16/odoo16/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo16.listing', {
#             'root': '/odoo16/odoo16',
#             'objects': http.request.env['odoo16.odoo16'].search([]),
#         })

#     @http.route('/odoo16/odoo16/objects/<model("odoo16.odoo16"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo16.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo16(models.Model):
    _name = 'odoo16.odoo16'
    _description = 'odoo16 odoo16'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()

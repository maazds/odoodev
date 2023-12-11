# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo16(models.Model):
    _name = 'odoo.16'
    _description = 'odoo16 odoo16'

    name = fields.Char('Name')
    age = fields.Integer('Age')
    ref = fields.Char('Ref')
    gender = fields.Selection([('0','Male'),('1','Female')],'Gender',required=True)
    active = fields.Boolean('Active' , default=True)

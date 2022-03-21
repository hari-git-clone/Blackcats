# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import strptime
from dateutil import parser

class blackcats(models.Model):
     _name = 'blackcats.blackcats'

     name = fields.Char(string="Name",required = True ,default="Name")
     phone = fields.Char(string="Phone Number",required = True)
     qualification= fields.Char(string="Qualification",required = True )
     dob = fields.Date(string="DOB",required = True )
     image = fields.Binary(string="image")
     work = fields.Selection([('yes',"Yes"),('no',"No")])
     ht = fields.Html(string="HTML")



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

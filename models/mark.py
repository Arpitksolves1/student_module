# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MarkData(models.Model):
    _name = "mark.data"
    _description = "Mark Data"

    name = fields.Many2one("student.data", string="Student Name")
    math = fields.Integer(string="Math")
    physics = fields.Integer(string="Physics")
    chemistry = fields.Integer(string="Chemistry")
    english = fields.Integer(string="English")
    hindi = fields.Integer(string="Hindi")



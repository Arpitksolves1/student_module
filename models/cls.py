# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ClassData(models.Model):
    _name = "class.info"
    _description = "Class Info"

    name = fields.Char(string="Class Name")
    subject1 = fields.Char(string="Subject1")
    subject2 = fields.Char(string="Subject2")
    subject3 = fields.Char(string="Subject3")
    subject4 = fields.Char(string="Subject4")
    subject5 = fields.Char(string="Subject5")
    student_name = fields.Many2one("student.data")


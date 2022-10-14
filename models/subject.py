# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SubjectData(models.Model):
    _name = "subject.data"
    _description = "Subject Data"

    name = fields.Char(string="Subject Name")

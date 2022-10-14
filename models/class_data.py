# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ClassData(models.Model):
    _name = "class.data"
    _description = "Class Data"

    name = fields.Selection(
        [("Class 8", "Class 8"), ("Class 9", "Class 9"), ("Class 10", "Class 10"), ("Class 11", "Class 11"),
         ("Class 12", "Class 12")],
        string="Class Name")
    class_fees = fields.Integer(string="Class Fess")

    # Selecting multiple subject for a class.
    # class_subject_ids = fields.Many2many("subject.data", "class_subject_data", "class_id", "subject_id",
    #                                      string="Subjects")

    class_student_line = fields.One2many("student.data", "student_class_id", string="student Details")

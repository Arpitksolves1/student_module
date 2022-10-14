# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StudentData(models.Model):
    _name = "student.data"
    _inherit = ['mail.thread']
    _description = "student Data "

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            student = self.env['student.data'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if student:
                raise ValidationError(('student %s already exist' % rec.name))

    _sql_constraints = {
        ('unique_name', 'unique(mobile)', 'Mobile number must be unique')
    }

    name = fields.Char(string="Name")
    age = fields.Char(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    dob = fields.Date(string="Dob")
    mobile = fields.Char(string="Mobile")
    student_fees = fields.Integer(string="student Fees")
    student_submitted_fees = fields.Integer(String="Submitted Fees", readonly=True)
    student_remaining_fees = fields.Integer(String="Remaining Fees", readonly=True)
    student_class_id = fields.Many2one("class.data", string="Class")
    student_mark_line = fields.One2many("mark.data", "name", string="Marks")
    fees_update_id = fields.Many2one("fees.data", string="Fees ")
    class_line = fields.One2many("class.info", "student_name", string="Class Name")
    db_user_id = fields.Many2one('res.users', string="User")

    # class_subject = fields.Many2many("subject.data', "name", string="Class Subject")
    # select_class = fields.Many2one("class.info", string="Class Name")

    @api.onchange("student_class_id")
    def onchange_student_class_id(self):
        if self.student_class_id:
            if self.student_class_id.class_fees:
                self.student_fees = self.student_class_id.class_fees
        else:
            self.student_fees = ''

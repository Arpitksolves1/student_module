# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StudentExcelReportWizard(models.TransientModel):
    _name = "student.report.wizard"
    _description = "student Report Wizard"

    name = fields.Char(string="Name")
    age = fields.Char(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    dob = fields.Date(string="Dob")
    mobile = fields.Char(string="Mobile")
    student_fees = fields.Integer(string="student Fees")
    student_submitted_fees = fields.Integer(String="Submitted Fees", readonly=True)
    student_remaining_fees = fields.Integer(String="Remaining Fees", readonly=True)
    student_class_line = fields.Many2one("class.data", string="Class")
    student_mark_line = fields.One2many("mark.data", "name", string="Marks")
    fees_update = fields.Many2one("fees.data", string="Fees ")
    class_id = fields.One2many("class.info", "student_name", string="Class Name")
    db_user = fields.Many2one('res.users', string="User")

    @api.model
    def default_get(self, field_list=[]):
        res = super(StudentExcelReportWizard, self).default_get(field_list)
        active_id = self._context.get('active_id')
        if active_id:
            student_id = self.env['student.data'].browse(active_id)
            res['name'] = student_id.name
            res['age'] = student_id.age
            res['gender'] = student_id.gender
            res['dob'] = student_id.dob
            res['mobile'] = student_id.mobile
            res['student_fees'] = student_id.student_fees
            res['student_submitted_fees'] = student_id.student_submitted_fees
            res['student_remaining_fees'] = student_id.student_remaining_fees
            res['student_class_line'] = student_id.student_class_line
            res['student_mark_line'] = student_id.student_mark_line
            res['class_id'] = student_id.class_id
            res['db_user'] = student_id.db_user

            return res

    def print_excel_report(self):
        data = {
            'form_data': self.read()[0]
        }
        return self.env.ref('student.student_report_excel_temp').report_action(self, data=data)

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FeesUpdates(models.Model):
    _name = "fees.data"
    _description = "Fees Update Data "

    # Get fees from student table
    @api.onchange("name")
    def onchange_student_class_id(self):
        if self.name.student_fees:
            self.fees = self.name.student_fees

    name = fields.Many2one("student.data", string="student Name")
    fees = fields.Integer(string="Fees")
    submit_fees = fields.Integer(string="Submit amount")
    submitted_fees = fields.Integer(string="submitted Fees", compute="_compute_submit_fees")
    remaining_fees = fields.Integer(string="Remaining Fees", compute="_compute_remaining_fees")
    old_fees = fields.Integer(String="Old Submitted Fees", store=True)

    # For computing submitted fees
    @api.depends("name")
    def _compute_submit_fees(self):
        for rec in self:
            if rec.submit_fees > rec.fees:
                rec.submit_fees = rec.fees

            rec.submitted_fees = rec.old_fees + rec.submit_fees

            # automatic update submitted fees in student table
            rec.name.student_submitted_fees = rec.submitted_fees
            rec.name.student_fees = rec.fees

    # For computing remaining fees
    @api.depends("name")
    def _compute_remaining_fees(self):
        for rec in self:
            rec.remaining_fees = rec.fees - rec.submitted_fees
            if rec.remaining_fees < 0:
                rec.remaining_fees = 0
            rec.old_fees = rec.submitted_fees

            # automatic update submitted fees in student table
            rec.name.student_remaining_fees = rec.remaining_fees
            rec.submit_fees = 0



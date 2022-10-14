# -*- coding: utf-8 -*-

from odoo import models


class StudentExcelReportView(models.AbstractModel):
    _name = 'report.student.student_excel_template'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, detail):
        ans = data['form_data']
        sheet = workbook.add_worksheet('Excel Student Report')
        bold = workbook.add_format({'bold': True})
        row = 0
        col = 0
        sheet.set_column('A:H', 12)

        sheet.write(row, col, 'Name', bold)
        sheet.write(row + 1, col, ans['name'])

        sheet.write(row, col + 1, 'Age', bold)
        sheet.write(row + 1, col + 1, ans['age'])

        sheet.write(row, col + 2, 'Date of Birth', bold)
        sheet.write(row + 1, col + 2, ans['dob'])

        sheet.write(row, col + 3, 'Gender', bold)
        sheet.write(row + 1, col + 3, ans['gender'])

        sheet.write(row, col + 4, 'Mobile', bold)
        sheet.write(row + 1, col + 4, ans['mobile'])

        sheet.write(row, col + 5, 'User', bold)

        sheet.write(row, col + 5, 'Student Submitted Fees', bold)
        sheet.write(row + 1, col + 5, ans['student_submitted_fees'])

        sheet.write(row, col + 5, 'Student Remaining Fees', bold)
        sheet.write(row + 1, col + 5, ans['student_remaining_fees'])

        # sheet.write(row, col + 5, 'Student Fees', bold)
        # sheet.write(row + 1, col + 5, ans['student_fees'])

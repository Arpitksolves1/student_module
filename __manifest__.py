# -*- coding: utf-8 -*-


{
    'name': 'student Details',
    'version': '1.0.0',
    'category': 'student',
    'sequence': 1,
    'summary': 'student Management System',
    'description': "All the details of students are present in this model",
    'depends': ['base', 'report_xlsx', 'mail'],
    'data': [
        "security/ir.model.access.csv",
        "security/security_rule.xml",
        'wizard/student_report_wizard_view.xml',
        'report/report.xml',
        "views/student_views.xml",
        "views/menu_view.xml",
        "views/subject_views.xml",
        "views/class_views.xml",
        "views/fees_update_views.xml",
        "views/mark_views.xml",
        "views/cls_views.xml"
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
}

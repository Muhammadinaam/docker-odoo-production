# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    # Module information
    "name": "HR Attendance OverTime",
    "version": "15.0.1.0.0",
    "live_test_url": "https://www.youtube.com/watch?v=0ayc26P8x9o",
    "category": "Human Resources",
    "description": """This module manage employee Overtime and attendance details.
                    Employee Overtime.
                    Employee attendance
                    Attendance OverTime""",
    "license": "LGPL-3",
    "summary": "Manage Employee over time and attendance.",
    'sequence': 1,

    # Author
    "author": "Serpent Consulting Services Pvt. Ltd.",
    'website': 'http://www.serpentcs.com',

    # Dependencies
    "depends": [
                "hr_holidays", "hr_attendance", "scs_hr_payroll", 'hr_contract',
    ],

    # Views
    "data": [
        "security/ir.model.access.csv",
        'data/hr_payroll_demo.xml',
        "views/hr_contract.xml",
        "views/hr_overtime_view.xml",
        "views/hr_attendance_policies_view.xml",
        "views/hr_attendance_sheet_view.xml",
        "wizard/change_attendance_data_view.xml",
    ],
    
    'images': ['static/description/banner_icon.jpg'],

    "installable": True,
    "auto_install": False,
    'price': 55,
    'currency': 'EUR',
}

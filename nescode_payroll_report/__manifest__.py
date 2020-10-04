# -*- coding: utf-8 -*-

{
    'name': 'Nescode Odoo13 Payroll Report',
    'category': 'Generic Modules/Human Resources',
    'version': '13.0.1.5.3',
    'author': 'Nescode',
    'company': 'Nescode',
    'maintainer': 'Nescode',
    
    'summary': 'Manage your employee payroll Report',
  
    'depends': [
        
        'hr_payroll_community'
    ],
    'data': [
        
        
        'views/hr_payroll_report.xml',
        'views/report_payslipdetails_templates.xml',
    ],
    
    # 'demo': ['data/hr_payroll_demo.xml'],
}

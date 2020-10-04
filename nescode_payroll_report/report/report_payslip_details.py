#-*- coding:utf-8 -*-

from odoo import api, models

class PayslipDetailsReportsNescode(models.AbstractModel):
    _name = 'report.nescode_payroll_report.report_payslipdetails_nescode'
    _description = 'Payslip Details Report'
    
   
    @api.model
    def _get_report_values(self, docids, data=None):
        payslips = self.env['hr.payslip'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.payslip',
            'docs': payslips,
            'data': data,
        
        }

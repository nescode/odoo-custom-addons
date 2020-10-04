# -*- coding:utf-8 -*-

import babel
from collections import defaultdict
from datetime import date, datetime, time
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone
from pytz import utc

from odoo import api, fields, models, tools, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_utils

# This will generate 16th of days
ROUNDING_FACTOR = 16


class HrSalaryRuleCategoryInherit(models.Model):
    _inherit = 'hr.salary.rule.category'
    _description = 'Salary Rule Category'

    type_select = fields.Selection([('allowance', 'Allowance'),('deduction','Deduction')])


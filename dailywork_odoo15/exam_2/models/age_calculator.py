from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class age_calculator(models.Model):
    _inherit = 'res.partner'

    Birth_date = fields.Date(string="Birth Date", default=date.today())
    today_date = fields.Date(string="Today", default=date.today())
    age = fields.Integer(compute='_compute_age')


    @api.depends("Birth_date", "today_date")
    def _compute_age(self):
        if self.Birth_date:
            diff = relativedelta(self.today_date,self.Birth_date)
            self.age = self.today_date.year - self.Birth_date.year
            self.age = diff.years
        else:
            self.age = 0

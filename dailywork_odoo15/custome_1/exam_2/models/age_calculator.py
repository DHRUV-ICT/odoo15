from odoo import models, fields, api
from datetime import date


class age_calculator(models.Model):
    _inherit = 'res.partner'

    Birth_date = fields.Date(string="Birth Date", default=date.today())
    today = fields.Date(string="Today", default=date.today())
    age = fields.Integer(compute='_compute_age')


    @api.depends("Birth_date", "today")
    def _compute_age(self):
        if self.Birth_date:
            self.age = self.today.year - self.Birth_date.year
        else:
            self.age = 0

from odoo.addons.portal.controllers import portal
from odoo.http import request

class EmployeePortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(EmployeePortal, self)._prepare_home_portal_values(counters)
        contract_count = request.env["hr.contract"].search_count([])
        values.update({
            'contract_count': contract_count
        })
        return values
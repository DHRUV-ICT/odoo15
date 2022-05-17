from odoo.addons.portal.controllers import portal
from odoo.http import request
from odoo import http

class EmployeePortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(EmployeePortal, self)._prepare_home_portal_values(counters)
        contract_count = request.env["hr.contract"].search_count([('employee_id', '=', request.env.user.employee_id.id)])
        values.update({
            'contract_count': contract_count
        })
        return values



    @http.route('/my/contracts', type='http', auth='user', website=True, csrf=False)
    def login_page(self, **kw):
        """Function to render the list template on the
        click of Contract portal."""
        contracts_list = request.env['hr.contract'].search([('employee_id', '=', request.env.user.employee_id.id)])
        return request.render('libary.portal_my_contracts', {
            'contracts_list': contracts_list
        })

    @http.route(['/my/contracts/details/<model("hr.contract"):contracts_list>'], type='http', auth='user', website=True)
    def contracts_details(self, contracts_list):
        """Function to render the details template and
        to link templates."""
        return request.render("libary.contracts_detail", {
            'details': contracts_list
        })
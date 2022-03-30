from odoo import models, fields, api


class res(models.Model):

    _inherit = 'sale.order'

    def schedule_action(self):
        print('#############################')

        if self.state == 'draft':
            self.search([]).write({'state':'sent'})


        # for rec in self:
        #     if rec.state == 'draft':
        #         rec.state = 'sent'
        #     print('#!!!!!!!!!!!!!!!!!!@!@@@@@!@!@')

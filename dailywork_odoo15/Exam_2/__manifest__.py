# -*- coding: utf-8 -*-
{
    'name': "Exam_2",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'sequence': '1',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/setting.xml',
        'wizard/views.xml',
        'views/server_action.xml',
        'views/age_calculator.xml',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'license': 'LGPL-3'
    , 'application': True
}

# -*- coding: utf-8 -*-
{
    'name': "U3A2",
    'summary': """U3A2""",
    'description': """
        ejericcio U3A2:
    """,
    'author': "Juan Compairé",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Custom',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
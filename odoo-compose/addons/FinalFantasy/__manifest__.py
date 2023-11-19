# -*- coding: utf-8 -*-
{
    'name': "FinalFantasy",
    'summary': """FinalFantasy""",
    'description': """
        FinalFantasy
    """,
    'author': "Juan Compaire",
    'website': "http://www.ilusion.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Prueba',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
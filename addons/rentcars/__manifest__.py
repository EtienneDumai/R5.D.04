# -*- coding: utf-8 -*-
{
    'name': "Location de voiture",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Location',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/rentcars_menu.xml',
        'views/vehicle_views.xml',
        'views/vehicle_list_template.xml',
        'views/garage_view.xml',
        'views/garage_kanban_view.xml',
        'views/reparation_kanban_view.xml',
        'security/rentcars_security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/rentcars.vehicle.csv',
        'demo/rentcars.garage.csv',
    ],
}


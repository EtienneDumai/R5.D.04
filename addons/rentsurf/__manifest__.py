# -*- coding: utf-8 -*-
{
    'name': "Location de planche de surf",
    'summary': "Gestion de quivers, boards, options et catégories",
    'description': """
Module de location de planches de surf :
- gestion des boards
- gestion des quivers (emplacements)
- options et catégories
- page web publique
""",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Services/Location',
    'version': '0.1',
    'depends': [
        'base',
        'website',
    ],
    'application': True,

    'data': [
        # Sécurité d'abord
        'security/rentsurf_security.xml',
        'security/ir.model.access.csv',

        # Menus / actions (souvent avant les vues si elles référencent les actions)
        'views/rentsurf_menu.xml',
        'views/board_kanban_views.xml',
        'views/board_list_template.xml',
        'views/res_partner_views.xml',
        # Vues backend
        'views/board_views.xml',
        'views/views.xml',

        # Template de liste backend (si utilisé par une vue custom)
        'views/board_list_template.xml',

        # Templates web (qweb)
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}

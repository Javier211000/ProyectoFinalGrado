# -*- coding: utf-8 -*-
{
    'name': "Fútbol",

    'summary': """
        Estadísticas de jugadores de Fútbol""",

    'description': """
        Módulo que te mostrará los goles logrados, los equipos en los que jugó,
        si está o no retirado, de un determinado jugador rellenando sus datos,
        este módulo sería tanto para móvil como para ordenador.
    """,

    'author': "Javier Alonso Fernández",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_equipo.xml',
        'reports/report_jugador.xml',
        'reports/report_temporada.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

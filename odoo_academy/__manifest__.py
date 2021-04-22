# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'description': """
        Academy Module to manage Training:
        -Courses
        -Session
        -Attendees
    """,
    
    'Author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['sale'],
    
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course.xml',
        'views/academy_menuitems.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml'
        
    ],
    
    'demo': [
        
        'demo/demo.xml'
    ],

    
}
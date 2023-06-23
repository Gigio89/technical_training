{
    'name': 'Odoo Academy',
    'summary': """Module to handle Course and Sessions""",
    'description': """Module to handle:
        - Courses
        - Sessions
        - Attendees
        """,
    'license': 'OPL-1',
    'author': 'Gigio89',
    'website': 'www.infinion.ch',
    'category': 'Custom Modules/Tech Training',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
        'views/session_views.xml',
    ],
    'application': True,
}
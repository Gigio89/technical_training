{
    'name': 'Cooperative Volunteers',
    'summary': """Cooperative Volunteers Module""",
    'description': """Exercise Training""",
    'license': 'OPL-1',
    'author': 'Gigio89',
    'website': 'www.infinion.ch',
    'category': 'Custom Modules/Tech Training',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/volunteer_groups.xml',
        'security/volunteer_security.xml',
        'security/ir.model.access.csv',
        'views/volunteer_menuitems.xml',
        'views/task_views.xml',
    ],
    'demo': [
        'demo/task_demo.xml',
    ],
    'application': True,
}
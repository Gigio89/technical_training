{
    'name': 'Spaceship Mission',
    'summary': """Odoo Space Mission""",
    'description': """Module to track different metrics of spaceship""",
    'license': 'OPL-1',
    'author': 'Gigio89',
    'website': 'www.infinion.ch',
    'category': 'Custom Modules/Tech Training',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/spaceship_groups.xml',
        'security/ir.model.access.csv',
        'security/spaceship_security.xml',
        'views/spaceship_menuitems.xml',
    ],
    'demo': [
        'demo/spaceship_demo.xml',
    ],
'application': True,
}
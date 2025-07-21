{
    'name': "Customer Support System",
    'version': '1.0.0',
    'summary': "System for managing customer requests and tickets.",
    'author': " stnc ",
    'website': "https://github.com/stnc",
    'category': 'Services/Helpdesk',
    'license': 'LGPL-3',

    'depends': ['base', 'mail', 'website'], 

    'data': [
        'security/ir.model.access.csv',
        'data/support_ticket_data.xml',
        'views/support_ticket_views.xml',
        'views/support_ticket_templates.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
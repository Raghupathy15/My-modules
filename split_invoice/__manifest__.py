
{
    'name': 'Account customization',
    'version': '1',
    'summary': """Customization In Account Invoice""",
    'description': 'This module helps you to add more information in account invoice records.',
    'category': 'Account',
    'author': 'Indglobal digital private limited',
    'company': 'Indglobal digital private limited',
    'website': "https://indglobal.in",
    'depends': ['base', 'account'],
    'data': [
                'wizards/split_invoices_views.xml',
                'views/account_move_view.xml',
        		# 'views/account_move_line_view.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}



{
    'name': 'Sale for Cookies in Odoo',
    'depends': [
        'base', 'sale',
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/sale_cookies_views.xml",
        "data/sale_cookies_menus.xml"
    ],
    'author': 'Manuel Jauregui',
    'category': 'Sales',
    'version': '1.0',
    'application': True,
    }
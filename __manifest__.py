# -*- coding: utf-8 -*-
{
    'name': "product_disc_restriction",

    'summary': "Duplicate proudct restriction and discount limit check",

    'description': """
Restrict the duplicate products on sale, purchase and invoice lines and also checks the discount limits exceeds for eacn products""",

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale', 'purchase', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_category_views.xml',
        'views/sale_order_views.xml',
    ],
}


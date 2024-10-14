from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    discount_limit = fields.Float(string="Discount Category")


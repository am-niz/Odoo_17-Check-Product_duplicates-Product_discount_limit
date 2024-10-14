from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    discount_limit = fields.Float(string="Discount Limit")
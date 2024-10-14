from odoo import fields, models, api, exceptions


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    discount = fields.Float(string="Disc %")

    @api.model
    def create(self, vals):
        lines = self.env["sale.order.line"].search_count([
            ("order_id", "=", vals.get("order_id")),
            ("product_id", "=", vals.get("product_id"))
        ])
        print("++++++++++++++++++", lines)
        if lines == 1:
            raise exceptions.ValidationError("You cannot add the same product to the sale order multiple times.")

        return super(SaleOrderLine, self).create(vals)

    @api.onchange("discount")
    def _onchange_discount(self):
        product_limit = self.product_template_id.discount_limit
        if self.discount > product_limit:
            raise exceptions.ValidationError("Product Discount Limit Exceeded")
        category_limit = self.product_template_id.categ_id.discount_limit
        if self.discount > category_limit:
            raise exceptions.ValidationError("Product Category Discount Limit Exceeded")
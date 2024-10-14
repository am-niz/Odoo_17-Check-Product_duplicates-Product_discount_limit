from odoo import models, api, exceptions


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.model
    def create(self, vals):
        order_id = vals.get("order_id")
        product_id = vals.get("product_id")
        print("order_id", order_id)
        print("product_id", product_id)
        lines = self.env["purchase.order.line"].search_count([
            ("order_id", "=", order_id),
            ("product_id", "=", product_id )
        ])
        print("purchase", lines)
        if lines == 1:
            raise exceptions.ValidationError("You cannot add the same product to the purchase order multiple times.")
        return super(PurchaseOrderLine, self).create(vals)
from odoo import fields, models, api, exceptions


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.model
    def create(self, vals):
        move_id = vals.get("move_id")
        product_id = vals.get("product_id")
        print("move_id", move_id)
        print("product_id", product_id)
        if move_id and product_id:  # because it trigger multiple times so product_id sometimes None that why 'and'
            lines = self.env["account.move.line"].search_count([
                ("move_id", "=", move_id),
                ("product_id", "=", product_id)
            ])
            print("invoice", lines)
            if lines == 1:
                raise exceptions.ValidationError("You cannot add the same product to the invoice order multiple times.")
        return super(AccountMoveLine, self).create(vals)
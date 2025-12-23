from odoo import models, fields


class HistoryClothingType(models.Model):
    _name = "history.clothing.type"
    _description = "Clothing Type"
    _order = "name"

    name = fields.Char(required=True)
    category_id = fields.Many2one(
        "history.clothing.category", string="Category", required=True
    )

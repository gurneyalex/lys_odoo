from odoo import models, fields


class HistoryClothingCategory(models.Model):
    _name = "history.clothing.category"
    _description = "Clothing Category"
    _order = "name"

    name = fields.Char(required=True)
    clothing_ids = fields.One2many(
        "history.clothing.type",
        "category_id",
        string="Clothings",
    )

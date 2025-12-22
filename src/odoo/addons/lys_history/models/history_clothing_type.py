from odoo import models, fields


class HistoryClothingType(models.Model):
    _name = "history.clothing.type"
    _description = "Clothing Type"

    name = fields.Char(required=True)

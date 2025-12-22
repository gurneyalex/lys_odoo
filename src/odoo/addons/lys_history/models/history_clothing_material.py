from odoo import models, fields


class HistoryClothingMaterial(models.Model):
    _name = "history.clothing.material"
    _description = "Clothing Material"

    name = fields.Char(required=True)

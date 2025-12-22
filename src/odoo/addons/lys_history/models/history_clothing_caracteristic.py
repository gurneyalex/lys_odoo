from odoo import models, fields


class HistoryClothingCaracteristic(models.Model):
    _name = "history.clothing.caracteristic"
    _description = "Clothing Caracteristic"

    name = fields.Char(required=True)

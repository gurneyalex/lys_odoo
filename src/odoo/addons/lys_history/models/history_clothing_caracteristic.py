from odoo import models, fields


class HistoryClothingCaracteristic(models.Model):
    _name = "history.clothing.caracteristic"
    _description = "Clothing Caracteristic, used as tags on a clothing purchase"

    name = fields.Char(required=True)

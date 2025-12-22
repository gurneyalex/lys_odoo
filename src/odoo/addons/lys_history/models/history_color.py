from odoo import models, fields


class HistoryColor(models.Model):
    _name = "history.color"
    _description = "Color"

    name = fields.Char(required=True)
    annotation = fields.Char()

from odoo import models, fields


class HistoryLocation(models.Model):
    _name = "history.location"
    _description = "Location"

    name = fields.Char(required=True)
    shortcut = fields.Char(help="a shortcut for quickly searching")
    notes = fields.Html()
    # parent location ?

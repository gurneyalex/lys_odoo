from odoo import models, fields


class HistoryPerson(models.Model):
    _name = "history.person"
    _description = "Person"

    name = fields.Char(required=True)
    shortcut = fields.Char(help="a shortcut for quickly searching")
    notes = fields.Html()

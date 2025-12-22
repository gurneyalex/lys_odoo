from odoo import models, fields


class HistorySourceAccount(models.Model):
    _name = "history.source.account"
    _description = "Source Account"

    name = fields.Char(required=True)
    date_start = fields.Date()
    date_end = fields.Date()
    currency_id = fields.Many2one("res.currency", string="main currency", required=True)
    code = fields.Char()
    notes = fields.Html()

from odoo import models, fields


class HistoryPurchase(models.AbstractModel):
    _name = "history.purchase"
    _description = "Purchase"

    account_id = fields.Many2one("history.source.account", required=True)
    source_page = fields.Char()
    currency_id = fields.Many2one(related="account_id.currency_id")
    price = fields.Monetary()
    date = fields.Date("Purchase Date")

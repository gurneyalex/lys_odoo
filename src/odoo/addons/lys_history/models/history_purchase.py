from odoo import models, fields


class HistoryPurchase(models.AbstractModel):
    _name = "history.purchase"
    _description = "Purchase"

    account_id = fields.Many2one(
        "history.source.account",
        required=True,
        default=lambda rec: rec._default_account_id(),
    )
    source_page = fields.Char()
    currency_id = fields.Many2one(related="account_id.currency_id")
    price = fields.Monetary()
    date = fields.Date("Purchase Date", default=lambda rec: rec._default_date())

    def _default_account_id(self):
        last_record = self.search([], order="id desc", limit=1)
        return last_record.account_id.id

    def _default_date(self):
        last_record = self.search([], order="id desc", limit=1)
        return last_record.date

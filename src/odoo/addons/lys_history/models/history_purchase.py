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
    currency_id = fields.Many2one(
        "res.currency",
        compute="_compute_currency_id",
        store=True,
        readonly=False,
    )

    @fields.depends("account_id", "currency_id")
    def _compute_currency_id(self):
        for rec in self:
            if not rec.currency_id and rec.account_id and rec.account_id.currency_id:
                rec.currency_id = rec.account_id.currency_id

    price = fields.Monetary()
    date = fields.Date("Purchase Date", default=lambda rec: rec._default_date())

    def _default_account_id(self):
        last_record = self.search([], order="id desc", limit=1)
        return last_record.account_id.id

    def _default_date(self):
        last_record = self.search([], order="id desc", limit=1)
        return last_record.date

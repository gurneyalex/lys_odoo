from odoo import models, fields


class HistorySourceAccount(models.Model):
    _name = "history.source.account"
    _description = "Source Account"

    name = fields.Char(required=True)
    date_start = fields.Date(default="1389-01-01")
    date_end = fields.Date(default="1390-01-01")
    currency_id = fields.Many2one(
        "res.currency",
        string="main currency",
        required=True,
        default=lambda rec: rec._default_currency_id(),
    )
    code = fields.Char()
    notes = fields.Html()

    def _default_currency_id(self):
        return self.env.ref("lys_history.res_currency_parisis").id

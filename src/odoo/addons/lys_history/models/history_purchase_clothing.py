from odoo import models, fields


class HistoryPurchaseClothing(models.Model):
    _name = "history.purchase.clothing"
    _inherit = "history.purchase"
    _description = "Purchase Clothing"

    person_id = fields.Many2one("history.person", string="Recipient")
    craftsman_id = fields.Many2one("history.person", string="Craftsman")
    name = fields.Char(required=True)
    type = fields.Many2one("history.clothing.type", required=True)

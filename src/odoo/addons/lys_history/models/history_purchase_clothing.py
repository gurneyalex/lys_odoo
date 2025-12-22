from odoo import models, fields


class HistoryPurchaseClothing(models.Model):
    _name = "history.purchase.clothing"
    _inherit = "history.purchase"
    _description = "Purchase Clothing"

    person_id = fields.Many2one("history.person", string="Recipient")
    craftsman_ids = fields.Many2many("history.person", string="Craftsmen")
    name = fields.Char(required=True)
    type = fields.Many2one("history.clothing.type", required=True)

    material_ids = fields.One2many("history.purchase.raw.material", "clothing_id")
    caracteristic_ids = fields.Many2many("history.clothing.caracteristic")

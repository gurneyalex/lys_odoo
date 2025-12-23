from odoo import api, fields, models


class HistoryPurchaseRawMaterial(models.Model):
    _name = "history.purchase.raw.material"
    _inherit = "history.purchase"
    _description = "Purchase Raw Material"

    name = fields.Char(required=True)
    usage = fields.Char()
    material_id = fields.Many2one("history.clothing.material")
    color_id = fields.Many2one("history.color")
    origin_id = fields.Many2one("history.location")
    currency_id = fields.Many2one(related="account_id.currency_id")
    unit_price = fields.Monetary()
    quantity = fields.Float()
    uom_id = fields.Many2one("uom.uom")
    clothing_id = fields.Many2one("history.purchase.clothing")
    supplier_id = fields.Many2one("history.person", string="Supplier")

    @api.depends("name", "material_id", "supplier_id", "date")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.material_id.name} - {record.name} ({record.supplier_id.name} {record.date})"

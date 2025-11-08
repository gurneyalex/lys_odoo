from odoo import models, fields


class HistorySourceAccount(models.Model):
    _name = "history.source.account"

    name = fields.Char(required=True)
    date_start = fields.Date()
    date_end = fields.Date()
    currency_id = fields.Many2one("res.currency", string="main currency", required=True)
    code = fields.Char()
    notes = fields.Html()



class HistoryLocation(models.Model):
    _name = "history.location"

    name = fields.Char(required=True)
    shortcut = fields.Char(help="a shortcut for quickly searching")
    notes = fields.Html()
    # parent location ?


class HistoryPerson(models.Model):
    _name = "history.person"

    name = fields.Char(required=True)
    shortcut = fields.Char(help="a shortcut for quickly searching")
    notes = fields.Html()

class HistoryPurchase(models.AbstractModel):
    _name = "history.purchase"
    account_id = fields.Many2one("history.source.account", required=True)
    source_page = fields.Char()
    currency_id = fields.Many2one(related="account_id.currency_id")
    price = fields.Monetary()
    date = fields.Date("Purchase Date")

class HistoryPurchaseClothing(models.Model):
    _name = "history.purchase.clothing"
    _inherit = "history.purchase"

    person_id = fields.Many2one(string="Recipient")
    craftsman_id = fields.Many2one(string="Craftsman")
    name = fields.Char(required=True)
    type = fields.Many2one("history.clothing.type", required=True)

class HistoryPurchaseRawMaterial(models.Model):
    _name = "history.purchase.raw.material"
    _inherit = "history.purchase"

    name = fields.Char(required=True)
    material_id = fields.Many2one("history.clothing.material")
    color_id = fields.Many2one("history.color")
    origin_id = fields.Many2one("history.location")
    currency_id = fields.Many2one(related="account_id.currency_id")
    unit_price = fields.Monetary()
    quantity = fields.Float
    uom_id = fields.Many2one("uom.uom")

class HistoryClothingType(models.Model):
    _name = "history.clothing.type"

    name=fields.Char(required=True)


class HistoryClothingMaterial(models.Model):
    _name = "history.clothing.material"

    name=fields.Char(required=True)


class HistoryColor(models.Model):
    _name = "history.color"

    name = fields.Char(required=True)
    annotation = fields.Char()

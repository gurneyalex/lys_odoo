from odoo import api, fields, models


class HistoryColor(models.Model):
    _name = "history.color"
    _description = "Color"

    name = fields.Char(required=True)
    sub_category = fields.Char()

    @api.depends("name", "sub_category")
    def _compute_display_name(self):
        for record in self:
            if record.sub_category:
                display_name = f"{record.name} ({record.sub_category})"
            else:
                display_name = record.name
            record.display_name = display_name

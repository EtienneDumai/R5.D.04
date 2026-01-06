from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    rentsurf_is_customer = fields.Boolean("RentSurf customer", default=False)

    rentsurf_level = fields.Selection(
        [
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
        ],
        string="Surf level",
    )

    rentsurf_preferred_quiver_id = fields.Many2one(
        "rentsurf.quiver",
        string="Preferred Quiver",
    )
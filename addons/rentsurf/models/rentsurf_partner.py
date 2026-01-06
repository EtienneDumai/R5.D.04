from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    rentsurf_is_customer = fields.Boolean("Client RentSurf", default=False)

    rentsurf_level = fields.Selection(
        [
            ("debutant", "Débutant"),
            ("intermediaire", "Intermédiaire"),
            ("avance", "Avancé"),
        ],
        string="Niveau de surf",
    )

    rentsurf_preferred_quiver_id = fields.Many2one(
        "rentsurf.quiver",
        string="Quiver préféré",
    )
from odoo import fields, models, api
import re
from odoo.exceptions import ValidationError


class RentSurfBoard(models.Model):
    _name = 'rentsurf.board'
    _description = 'Description of board'

    active = fields.Boolean("Actif ?", default=True)

    # Champs textuels
    num_inv = fields.Char("Numero d'inventaire")
    model = fields.Char("Model")
    notes = fields.Text("Notes")

    # Champs numériques
    length_cm = fields.Float("Length (cm)")

    # Date
    date_purchased = fields.Date(string="Purchase Date")

    # Image
    thumbnail = fields.Binary("Thumbnail")

    # Select
    condition = fields.Selection(
        [
            ("new", "New"),
            ("good", "Good"),
            ("used", "Used"),
            ("damaged", "Damaged"),
        ],
        string="Condition",
        default="good",
        required=True,
    )

    # Relations
    quiver_id = fields.Many2one('rentsurf.quiver', string="Quiver")
    option_ids = fields.Many2many("rentsurf.option", string="Option of board")
    category_ids = fields.Many2many("rentsurf.category", string="Category of board")

    # Related (exigé)
    quiver_city = fields.Char(
        string="Quiver City",
        related="quiver_id.address_city",
        store=True,
        readonly=True,
    )

    # Calculé (exigé)
    age_days = fields.Integer(
        string="Age (days)",
        compute="_compute_age_days",
        store=True,
        readonly=True,
    )

    # Champs utilisés pour la visibilité conditionnelle dans la vue
    damage_report = fields.Text("Damage report")
    manager_internal_notes = fields.Text("Internal notes (manager)")

    @api.depends("date_purchased")
    def _compute_age_days(self):
        today = fields.Date.today()
        for rec in self:
            if rec.date_purchased:
                rec.age_days = (today - rec.date_purchased).days
            else:
                rec.age_days = 0

    def _check_num_inv(self):
        self.ensure_one()
        pattern = re.compile(r"^SURF-\d{4}-\d{4}$")
        return bool(self.num_inv and pattern.match(self.num_inv))

    def button_check_num_inv(self):
        for board in self:
            if not board.num_inv:
                raise ValidationError("Please provide a Numero d'inventaire for this board")
            if board.num_inv and not board._check_num_inv():
                raise ValidationError("%s Numero d'inventaire is invalid" % (board.num_inv))
        return True

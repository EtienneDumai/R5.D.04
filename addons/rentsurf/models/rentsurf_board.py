from odoo import fields, models
import re
from odoo.exceptions import ValidationError
class RentSurfBoard(models.Model):
    _name = 'rentsurf.board'
    _description='Description of board'
    active = fields.Boolean("Actif ?", default=True)
    num_inv = fields.Char("Numero d'inventaire")
    date_purchased = fields.Date(string="Purchase Date")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")
    garage_id = fields.Many2one('rentsurf.quiver', string="quiver")
    option_ids = fields.Many2many(
    "rentsurf.option",
    string="Option of board"
    )
    category_ids = fields.Many2many(
    "rentsurf.category",
    string="Category of board"
    )
    def _check_num_inv(self) :
        self.ensure_one() #vérifie que quel self contient 1 seul record.
        pattern = re.compile("^SURF-\d{4}-\d{4}$")
        return pattern.match(self.num_inv)
    def button_check_num_inv(self):
        for board in self:
            if not board.num_inv:
                raise (ValidationError("Please provide a Numero d'inventaire for this board"))
            if board.num_inv and not board._check_num_inv():
                raise ValidationError("%s Numero d'inventaire is invalid" % (board.num_inv))
        return True


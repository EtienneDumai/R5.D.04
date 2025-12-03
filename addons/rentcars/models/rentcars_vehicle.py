from odoo import fields, models, api
import re
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
class RentcarsVehicle(models.Model):
    _name = 'rentcars.vehicle'
    _description='Description of vehicle'
    active = fields.Boolean("Actif ?", default=True)
    immatriculation = fields.Char('Numberplate')
    date_purchased = fields.Date(string="Purchase Date")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")
    age_vehicle=fields.Integer(compute="_age_vehicle", string="Age of vehicle (years)")
    garage_id = fields.Many2one('rentcars.garage', string="garage")
    option_ids = fields.Many2many(
    "rentcars.option",
    string="Option of vehicle"
    )
    category_ids = fields.Many2many(
    "rentcars.category",
    string="Category of vehicle"
    )
    garage_city = fields.Char(related='garage_id.address_city', string="Garage City")
    state=fields.Selection([
    ('broken', 'Broken Down'),
    ('repaired', 'Being repaired'),
    ('usable', 'Usabled')])
    repairing_status=fields.Selection([
    ('arrived', 'Just arrived'),
    ('diagnoses','Diagnosing'),
    ('waiting', 'Waiting for parts'),
    ('repairing', 'Repairing'),
    ('finish', 'Finish')
    ], string="Repairing status", default='arrived')
    @api.depends('date_purchased')
    def _age_vehicle(self):
        for vehicle in self:
            TODAY = date.today()
            vehicle.age_vehicle=relativedelta(TODAY,vehicle.date_purchased).years
    def _check_immatriculation(self) :
        self.ensure_one() #vérifie que quel self contient 1 seul record.
        pattern = re.compile("^\w{2}[0-9]{3}\w{2}$")
        return pattern.match(self.immatriculation)
    def button_check_immatriculation(self):
        for vehicle in self:
            if not vehicle.immatriculation:
                raise (ValidationError("Please provide an Numberplate for this car"))
            if vehicle.immatriculation and not vehicle._check_immatriculation():
                raise ValidationError("%s Numberplate is invalid" % (vehicle.immatriculation))
        return True


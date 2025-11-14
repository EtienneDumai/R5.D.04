from odoo import fields, models
import re
from odoo.exceptions import ValidationError
class RentcarsVehicle(models.Model):
    _name = 'rentcars.vehicle'
    _description='Description of vehicle'
    active = fields.Boolean("Actif ?", default=True)
    immatriculation = fields.Char('Numberplate')
    date_purchased = fields.Date(string="Purchase Date")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")
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


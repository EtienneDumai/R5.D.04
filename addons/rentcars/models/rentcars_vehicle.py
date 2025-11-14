from odoo import fields, models
class RentcarsVehicle(models.Model):
    _name = 'rentcars.vehicle'
    _description='Description of vehicle'
    active = fields.Boolean("Actif ?", default=True)
    immatriculation = fields.Char('Numberplate')
    date_purchased = fields.Date(string="Purchase Date")
    model = fields.Char("Model")
    thumbnail = fields.Binary("Thumbnail")

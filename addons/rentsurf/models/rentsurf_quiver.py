# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Quiver(models.Model):
    _name = 'rentsurf.quiver'
    _description = 'Un quiver de planches de surf'
    name= fields.Char("Nom")
    active=fields.Boolean("Actif ?", default=True)
    address_street = fields.Char("Rue")
    address_zipcode = fields.Char("Code postal")
    address_city = fields.Char("Ville")
    places_max = fields.Integer("Nombre de places")
    board_ids = fields.One2many("rentsurf.board", "quiver_id", string="Planches stockées")
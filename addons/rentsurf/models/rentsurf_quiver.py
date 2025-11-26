# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Quiver(models.Model):
    _name = 'rentsurf.quiver'
    _description = 'A quiver is a location for board'
    name= fields.Char("Name")
    active=fields.Boolean("Actif ?", default=True)
    address_street = fields.Char("Street")
    address_zipcode = fields.Char("Zip code")
    address_city = fields.Char("City")
    places_max = fields.Integer("No. of places")
    board_ids = fields.One2many("rentsurf.board", "quiver_id", string="parked boards")
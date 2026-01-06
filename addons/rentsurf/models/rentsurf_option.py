# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Option(models.Model):
    _name = 'rentsurf.option'
    _description = 'Option de planche de surf'
    active=fields.Boolean("Actif ?", default=True)
    name = fields.Char("Nom")
    category = fields.Selection([("security", "Sécurité"), ("comfort", "Confort"), ("aestheticism", "Esthétique")])
    description= fields.Char("Description")
    board_ids = fields.Many2many(
    "rentsurf.board",
    string="Planche avec option"
    )
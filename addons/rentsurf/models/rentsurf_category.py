# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Category(models.Model):
    _name = 'rentsurf.category'
    _description = 'Catégorie de planche de surf'
    _parent_store = True

    active=fields.Boolean("Actif ?", default=True)
    name = fields.Char("Nom")
    description= fields.Char("Description")

    vehicle_ids = fields.Many2many(
        "rentsurf.board",
        string="Planche avec option"
    )
    parent_id = fields.Many2one(
        "rentsurf.category",
        "Catégorie parente",
        ondelete="restrict")
    parent_path = fields.Char(index=True)

    # Optionnel, mais utile:
    child_ids = fields.One2many(
        "rentsurf.category",
        "parent_id",
        "Sous-catégories")
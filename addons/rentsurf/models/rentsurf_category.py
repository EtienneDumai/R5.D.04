# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Category(models.Model):
    _name = 'rentsurf.category'
    _description = 'Category of board'
    _parent_store = True

    active=fields.Boolean("Actif ?", default=True)
    name = fields.Char("Name")
    description= fields.Char("Description")

    vehicle_ids = fields.Many2many(
        "rentsurf.board",
        string="Board With option"
    )
    parent_id = fields.Many2one(
        "rentsurf.category",
        "Parent Category",
        ondelete="restrict")
    parent_path = fields.Char(index=True)

    # Optionnel, mais utile:
    child_ids = fields.One2many(
        "rentsurf.category",
        "parent_id",
        "Subcategories")
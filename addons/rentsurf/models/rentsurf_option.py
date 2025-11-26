# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Option(models.Model):
    _name = 'rentsurf.option'
    _description = 'Options of board'
    active=fields.Boolean("Actif ?", default=True)
    name = fields.Char("Name")
    category = fields.Selection([("security", "security"), ("comfort", "comfort"), ("aestheticism", "aestheticism")])
    description= fields.Char("Description")
    board_ids = fields.Many2many(
    "rentsurf.board",
    string="Board With option"
    )
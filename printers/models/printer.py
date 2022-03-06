# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Printers(models.Model):
    _name = "printer"
    _description = "Printers"

    name = fields.Char(string="Name", required=True, copy=False)
    type = fields.Selection(string="Type", required=True,
                            selection="[('fdm', 'FDM'), ('sla', 'SLA')]")

    'brand = many2one'


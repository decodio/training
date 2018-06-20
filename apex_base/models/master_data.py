# -*- coding: utf-8 -*-
# Copyright 2018 Decodio
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class Employee(models.Model):
    _name = "hr.employee"
    _description = "Employee"

    code = fields.Char('Code', help='Employee barcode')
    name = fields.Char('Code')
    active = fields.Boolean('Active', default=True)

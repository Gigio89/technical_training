from odoo import fields, models

class Spaceship(models.Model):
    _name = "spaceship.spaceship"
    _description = "Track the different metrics of the Spaceship"

    name = fields.Char("Title",required=True)
    active = fields.Boolean(string="Active",default=True)
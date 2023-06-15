from odoo import fields, models

class Task(models.Model):
    _name = "volunteer.task"
    _description = "Odoo Technical Training"

    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)
    


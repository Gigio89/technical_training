from odoo import fields, models

class Spaceship(models.Model):
    _name = "spaceship.spaceship"
    _description = "Track the different metrics of the Spaceship"

    name = fields.Char("Title",required=True)
    active = fields.Boolean(string="Active",default=True)
    type = fields.Selection(string="Ship Type",
                            selection=[
                                ('freighter','Freighter'),
                                ('transport','Transport'),
                                ('scout_ship','Scout Ship'),
                                ('fighter','Fighter'),
                            ],)
    model = fields.Char(string="Ship Model",required=True)
    build_date = fields.Date(string="Build Date")
    captain = fields.Char(string="Captain")
    required_crew = fields.Integer(string="Required Crew",default=1)
    length = fields.Float(string="Length")
    width = fields.Float(string="Width")
    height = fields.Float(string="Height")
    engine_number = fields.Char(string="Engine Number")
    fuel_type = fields.Selection(string="Fuel Type",
                                 selection=[
                                     ('solid_fuel','Solid Fuel'),
                                     ('liquid_fuel','Liquid Fuel'),                                     
                                 ],)
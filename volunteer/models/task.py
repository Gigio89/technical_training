from odoo import fields, models

class Task(models.Model):
    _name = "volunteer.task"
    _description = "Odoo Technical Training"

    name = fields.Char(string="Title", required=True)
    
    start_time = fields.Datetime(string="Start Time")
    stop_time = fields.Datetime(string="Stop Time")
    occurences = fields.Integer(string="Occurences")
    description = fields.Text(string="Description")
    task_type = fields.Selection(string="Task Type",
                                 selection=[
                                     ('to_do','To Do'),
                                     ('project','Project'),
                                     ('meeting','Meeting'),
                                 ],)
    

    
    


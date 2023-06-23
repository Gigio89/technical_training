from odoo import api, fields, models

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'
    
    name = fields.Char(string='Title', required=True)
    session_number = fields.Char(string="Session Number", default="S0000", copy=False, required=True, readonly=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('session_number', ('S0000')) == ('S0000'):
                vals['session_number'] = self.env['ir.sequence'].next_by_code('session.number')
                return super().create(vals_list)
            
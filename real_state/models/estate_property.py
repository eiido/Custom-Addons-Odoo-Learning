from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True)
    expected_price = fields.Float(string='Expected Price')
    bedroom = fields.Integer(string='Bedrooms', default=2)
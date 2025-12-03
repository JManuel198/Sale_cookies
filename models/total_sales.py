from odoo import models, fields, api

class TotalSales(models.Model):
    _name = 'total.money.sales'
    _description = 'Total money sales'

    name = fields.Char(string='Sale Order', required=True)
    total_revenue = fields.Float(string='Total Revenue', compute='_compute_total_revenue', store=True)

    @api.depends('sales.cookies.price_total')
    def _compute_total_revenue(self):
        for record in self:
            record.total_revenue = sum(line.total_price for line in record.sales.cookies)
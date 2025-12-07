from odoo import models, fields, api, _

class SaleCookies(models.Model):
    _name = 'sale.cookies'
    _description = 'Sales cookies'

    name = fields.Char()
    reference = fields.Char(readonly=True, default=lambda self: _('New'))
    description = fields.Text()
    active = fields.Boolean(default=True)

    client_id = fields.Many2one(comodel_name="res.partner", ondelete="restrict")

    product = fields.Selection(string="Product", selection=[
        ('choco_chips', 'Choco Chips'),
        ('choco_brownie', 'Choco Brownie'),
        ('red_velvet', 'Red Velvet'),
        ('brownie_clasico', 'Brownie clásico'),
        ('alfajores', 'Alfajores'),
        ('galletas_rellenas', 'Galletas Rellenas'),
    ], required=True)

    date_sale = fields.Date(string="Sale Date", required=True, default=fields.Date.context_today)
    status = fields.Selection(string="Status sale", selection=[
        ('pagado', 'Pagado'),
        ('pendiente', 'Pendiente')
    ], required=True)

    # Campos para la venta de galletas.
    
    # Calcular el precio unitario por gramo y el precio total.
    # Se pone el precio unitario según el gramaje del producto.
    # El precio total es cantidad * precio unitario.
    quantity = fields.Integer(string="Quantity", required=True, default=1)
    grams = fields.Integer(string="Grams", required=True)
    unit_price = fields.Float(string="Unit Price by gram", required=True)
    total_price = fields.Float(string="Total Price Sale", compute="_compute_total_price", readonly=True)

    @api.depends('quantity', 'unit_price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.quantity * record.unit_price
            
    # Campo para secuenciar el campo reference.
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Si viene como New (tu default), asigna secuencia
            if vals.get('reference', 'New') == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('sale.cookies') or _('New')
        return super().create(vals_list)
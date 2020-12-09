from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare

class AccountMove(models.Model):
	_inherit = "account.move"

	def compute_count(self):
		for record in self:
			record.split_inv_count = self.env['account.move'].search_count([('inv_split_ref','=',self.name)])

	inv_split_ref = fields.Char('Invoice Split Ref No',readonly=True)
	split_inv_count = fields.Integer('Split Invoice count',compute='compute_count')
				
	def get_split_inv_count(self):
		self.ensure_one()
		return {
			'type': 'ir.actions.act_window',
			'name': 'Split Count',
			'view_mode': 'tree,form',
			'res_model': 'account.move',
			'domain': [('inv_split_ref','=',self.name)],
			'context': "{'create': False}"
		}
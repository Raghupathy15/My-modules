# -*- coding: utf-8 -*-
import logging
from odoo import models, api,fields
from datetime import date, timedelta

class SplitInvoices(models.TransientModel):
	_name = 'split.invoices'
	_description = "Wizard - Split Invoices"

	inv_num = fields.Char(string='Invoice No',readonly=True)
	split_line_id = fields.One2many('split.line','split_id',string='Product Line')

	@api.model
	def default_get(self, fields):
		res = super(SplitInvoices, self).default_get(fields)
		inv_id = self.env['account.move'].browse(self._context.get('active_ids'))
		res.update({'inv_num':inv_id.name})
		return res

	def action_split_inv(self):
		inv = self.env['account.move']
		inv_line = self.env['account.move.line']
		if self.split_line_id.partner_id:
			for rec in self.split_line_id:
				inv_obj = inv.create({'partner_id':rec.partner_id.id,
									'type':'out_invoice',
									'inv_split_ref':self.inv_num,
									'journal_id':1,
									'invoice_date':fields.Date.today()})
				for data in rec.product_ids:
					inv_line_obj = inv_line.create({'product_id':data.id,
													'move_id':inv_obj.id,
													'name':data.name,
													'account_id':1,
													'price_unit':data.lst_price,
													'quantity':rec.quantity})
				parent_inv = self.env['account.move'].sudo().search([('name','=',self.inv_num)])
				if parent_inv:
					parent_inv.write({'state':'cancel'})

class SplitLine(models.TransientModel):
	_name = "split.line"

	product_ids = fields.Many2many('product.product',string='Product',required=True)
	partner_id = fields.Many2one('res.partner', string='Customer',required=True)
	quantity = fields.Float(string='Quantity')
	split_id = fields.Many2one('split.invoices',string='Split Invoices')

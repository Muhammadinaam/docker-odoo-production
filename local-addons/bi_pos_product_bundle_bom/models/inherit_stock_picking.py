# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api,tools, _
from datetime import datetime, timedelta
import json
from odoo.exceptions import Warning
import logging
from odoo.tools import float_is_zero

from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare

from itertools import groupby
_logger = logging.getLogger(__name__)


class RelatedPosStock(models.Model):
	_inherit = 'stock.picking'

	def _prepare_stock_move_vals_for_sub_product(self,first_line,item,order_lines):
		return {
			'name': first_line.name,
			'product_uom': item.product_uom_id.id,
			'picking_id': self.id,
			'picking_type_id': self.picking_type_id.id,
			'product_id': item.product_id.id,
			'product_uom_qty': item.qty * first_line.qty,
			'state': 'draft',
			'location_id': self.location_id.id,
			'location_dest_id': self.location_dest_id.id,
			'company_id': self.company_id.id,
		}

	def _create_move_from_pos_order_lines(self, lines):
		self.ensure_one()
		lines_by_product = groupby(sorted(lines, key=lambda l: l.product_id.id), key=lambda l: l.product_id.id)
		for product, lines in lines_by_product:
			
			order_lines = self.env['pos.order.line'].concat(*lines)
			
			first_line = order_lines[0]
			Move = self.env['stock.move']
			Move = Move.create(
				self._prepare_stock_move_vals(first_line, order_lines)
			)

			if first_line.product_id.bom_product:
				bom_product_list = self.env['bom.product'].search([('bom_product_id.id','=', first_line.product_id.id)])
				if bom_product_list.state == 'confirm':
					for item in bom_product_list.sub_products_ids:
						Move += Move.create(
							self._prepare_stock_move_vals_for_sub_product(first_line,item, order_lines)
						)
			
			confirmed_moves = Move._action_confirm()
			for move in confirmed_moves:
				if first_line.product_id == move.product_id and first_line.product_id.tracking != 'none':
					if self.picking_type_id.use_existing_lots or self.picking_type_id.use_create_lots:
						for line in order_lines:
							sum_of_lots = 0
							for lot in line.pack_lot_ids.filtered(lambda l: l.lot_name):
								if line.product_id.tracking == 'serial':
									qty = 1
								else:
									qty = abs(line.qty)
								ml_vals = move._prepare_move_line_vals()
								ml_vals.update({'qty_done':qty})
								if self.picking_type_id.use_existing_lots:
									existing_lot = self.env['stock.production.lot'].search([
										('company_id', '=', self.company_id.id),
										('product_id', '=', line.product_id.id),
										('name', '=', lot.lot_name)
									])
									if not existing_lot and self.picking_type_id.use_create_lots:
										existing_lot = self.env['stock.production.lot'].create({
											'company_id': self.company_id.id,
											'product_id': line.product_id.id,
											'name': lot.lot_name,
										})
									ml_vals.update({
										'lot_id': existing_lot.id,
									})
								else:
									ml_vals.update({
										'lot_name': lot.lot_name,
									})
								self.env['stock.move.line'].create(ml_vals)
								sum_of_lots += qty
							if abs(line.qty) != sum_of_lots:
								difference_qty = abs(line.qty) - sum_of_lots
								ml_vals = current_move._prepare_move_line_vals()
								if line.product_id.tracking == 'serial':
									ml_vals.update({'qty_done': 1})
									for i in range(int(difference_qty)):
										self.env['stock.move.line'].create(ml_vals)
								else:
									ml_vals.update({'qty_done': difference_qty})
									self.env['stock.move.line'].create(ml_vals)
					else:
						move._action_assign()
						sum_of_lots = 0
						for move_line in move.move_line_ids:
							move_line.qty_done = move_line.product_uom_qty
							sum_of_lots += move_line.product_uom_qty
						if float_compare(move.product_uom_qty, move.quantity_done, precision_rounding=move.product_uom.rounding) > 0:
							remaining_qty = move.product_uom_qty - move.quantity_done
							ml_vals = move._prepare_move_line_vals()
							ml_vals.update({'qty_done':remaining_qty})
							self.env['stock.move.line'].create(ml_vals)

				else:
					move.quantity_done = move.product_uom_qty

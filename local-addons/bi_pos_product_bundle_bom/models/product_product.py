# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api,_
from datetime import datetime,timezone


class CustomPOS(models.Model):
	_inherit = 'product.template'

	bom_product = fields.Boolean(
		string='POS BOM Product'
	)
# -*- coding: utf-8 -*-
#################################################################################
#
#  Copyright (c) 2020-Present RobertaBtt https://github.com/RobertaBtt)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#################################################################################

from odoo import fields, models, api
from odoo.exceptions import UserError

class DynamoDbConfigTable(models.Model):

    _name = "dynamodb.config.table"

    name = fields.Char(string='Name', compute="_get_name",store=True,readonly=True)

    resource_name=fields.Char(string="Resource Name", required=True)
    region_name=fields.Char(string="Region Name", required=True)
    endpoint = fields.Char(string="Endpoint", required=True)
    table_name=fields.Char(string="Table Name", required=True)
    table_key=fields.Char(string="Table Key", required=True)
    is_test=fields.Boolean(string="Is Test", required=True)


    @api.model
    def create(self, vals):
        config = self.env['dynamodb.config.table'].search( [('is_test', '=', True)])
        if config is not None and config.id:
            raise UserError("A table Test was already created")
        return super(DynamoDbConfigTable, self).create(vals)


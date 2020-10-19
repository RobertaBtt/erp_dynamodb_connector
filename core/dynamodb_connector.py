# -*- coding: utf-8 -*-
#################################################################################
#
#  Copyright (c) 2020-Present RobertaBtt https://github.com/RobertaBtt)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#################################################################################
import boto3
import json
import os
from odoo.exceptions import UserError

class DynamodbConnector:

    @staticmethod
    def dynamodb_connect(odoo_environment):

        config = odoo_environment["dynamodb.config.table"].sudo().search([('is_test', '=', True)])
        if config is None and not config.id:
            raise UserError("A table Test was already created")

        dynamodb = config['resource_name']
        region = config['region_name']
        tableName = config['table_name']
        tableKey = config['table_key']

        response = None
        try:
            dynamodb = boto3.resource(dynamodb, region_name=region)
            table = dynamodb.Table(tableName)
            response = table.get_item(Key={tableKey: 'ES000000091'})
        except Exception as ex:
            print(ex)

        return response
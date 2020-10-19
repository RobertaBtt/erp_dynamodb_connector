# -*- coding: utf-8 -*-
#################################################################################
#
#  Copyright (c) 2020-Present RobertaBtt https://github.com/RobertaBtt)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#################################################################################
import boto3
from odoo import api, fields, models, _


class DynamoDbTestResult(models.Model):
    _name = 'dynamodb.test.result'
    _description = 'DynamoDb Test'

    result = fields.Text('Result', readonly=True)



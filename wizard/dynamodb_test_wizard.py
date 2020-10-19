# -*- coding: utf-8 -*-
#################################################################################
#
#  Copyright (c) 2020-Present RobertaBtt https://github.com/RobertaBtt)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#################################################################################

import boto3
from odoo import api, fields, models, _

from ..core.dynamodb_connector import DynamodbConnector

class DynamoDbTestWizard(models.TransientModel):
    _name = 'dynamodb.test.wizard'
    _description = 'DynamoDb Test'

    def test_connection(self):


        result_connection = DynamodbConnector.dynamodb_connect(self.env)

        self.env['dynamodb.test.result'].create({'result': result_connection})

        tree_view_id = self.env.ref('erp_dynamodb_connector.view_dynamodb_test_result_tree').id
        form_view_id = self.env.ref('erp_dynamodb_connector.view_dynamodb_test_result_form').id


        action = {
            'type': 'ir.actions.act_window',
            'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'view_mode': 'tree,form',
            'name': _('DynamoDb Test Result'),
            'res_model': 'dynamodb.test.result',
            'domain': "",
            'context': dict(self.env.context),
        }
        return action

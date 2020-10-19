# -*- coding: utf-8 -*-
#################################################################################
#
#  Copyright (c) 2020-Present RobertaBtt https://github.com/RobertaBtt)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#################################################################################
{
    'name': 'DynamoDb Connector',
    'category': 'Tools',
    'summary': 'Your Connection to AWS DynamoDB',
    'website': 'https://github.com/RobertaBtt/erp_dynamodb_connector',
     'description': """
Dynamo DB ERP Connector
=======================

This module allows Odoo to connect to a table of DynamoDB to retrieve data. It is possible
 to test the connection using a Wizard.

""",
    'depends': ['base'],
    'external_dependencies': {'python': ['boto3']},
    'data': [
          'security/security.xml',
          'security/ir.model.access.csv',
          'views/dynamodb_connector_views.xml',
          'wizard/dynamodb_test_wizard.xml',

    ],
    'application': True,
    'installable': True,
}

import unittest
import json
import boto3


class TestConnection(unittest.TestCase):


    def test_connection(self):
        with open('../static/configuration/configuration_test.json') as config_file:
            data = json.load(config_file)

        dynamodb = data['resource']
        region=data['region']
        tableName = data['tableName']
        tableKey = data['tableKey']

        response = None
        try:
            dynamodb = boto3.resource(dynamodb, region_name=region)
            table = dynamodb.Table(tableName)
            response = table.get_item(Key={tableKey: 'ES000000091'})
        except Exception as ex:
            print(ex)


        self.assertNotEqual(None, response)
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(response['Item']['SerialNumber'], 'ES000000091')
        self.assertEqual(response['Item']['Timestamp_ISO8601'], '2020-10-03T19:16:19+00:00')
        self.assertEqual(response['Item']['Values']['t1'], '000045')

        try:
            response = table.scan()
            data = response['Items']

            while response.get('LastEvaluatedKey'):
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                data.extend(response['Items'])

        except Exception as ex:
             print(ex)

        self.assertNotEqual(None, response)
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(len(response["Items"]), 1)



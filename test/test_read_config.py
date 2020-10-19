import unittest
import json

class TestStringMethods(unittest.TestCase):

    def test_read_config(self):
        with open('../static/configuration/configuration_test.json') as config_file:
            data = json.load(config_file)

        self.assertEqual("dynamodb", data['resource'])
        self.assertEqual("stage", data['environment'])
        self.assertEqual("Test", data['tableName'])


if __name__ == '__main__':
    unittest.main()

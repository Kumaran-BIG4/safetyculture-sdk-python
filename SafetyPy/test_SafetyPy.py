# coding=utf-8
# Author: SafetyCulture
# Copyright: © SafetyCulture 2016

import unittest
import SafetyPy as sp

sc_client = sp.safetyculture()

class SafetyPyTestCase(unittest.TestCase):

    def test_parse_malformed_api_token(self):
        for bad_token in ['123', '111z09cg1e29c43hb77ea0di52ae37988c13f4b7fa6f6f59e9a1649141ef5132', '', None, 123]:
            config = {'API' : {'token' : bad_token}}
            self.assertIsNone(sc_client.parse_api_token(config))
            self.assertIsNone(sc_client.parse_api_token(config))

    def test_parse_missing_api_token(self):
        for config in ['', None]:
            self.assertIsNone(sc_client.parse_api_token(config))
            self.assertIsNone(sc_client.parse_api_token(config))


if __name__ == '__main__':
    unittest.main()
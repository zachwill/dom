#!/usr/bin/env python

import sys
import unittest
from domainr import Domain


search_result = ['goo', 'goo.gl', 'goo.gle', 'goog', 'google', 'google.com', 'google.net', 'google.org', 'google.us']
status_result = ['\x1b[31m✗\x1b[0m  goo', '\x1b[31m✗\x1b[0m  goo.gl', '\x1b[31m✗\x1b[0m  goo.gle',
                 '\x1b[31m✗\x1b[0m  goog', '\x1b[31m✗\x1b[0m  google', '\x1b[31m✗\x1b[0m  google.com',
                 '\x1b[31m✗\x1b[0m  google.net', '\x1b[31m✗\x1b[0m  google.org', '\x1b[31m✗\x1b[0m  google.us']


class TestDomain(unittest.TestCase):

    def setUp(self):
        sys.argv = ['core.py', 'google']

    def tearDown(self):
        sys.argv = []

    def test_search(self):
        env = Domain._get_argparser().parse_args()
        domain = Domain()
        result = domain.search(env)
        self.assertEquals(result, search_result)

    def test_status(self):
        env = Domain._get_argparser().parse_args()
        env.query = search_result
        domain = Domain()
        result = domain.status(env)
        self.assertEquals(result, status_result)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import sys
import unittest
import simplejson as json
from argparse import Namespace
from mock import MagicMock
from domainr import Domain

content = '{"query":"google","results":[{"domain":"google","host":"","subdomain":"google","path":"","availability":"tld","register_url":"http://domai.nr/google/register"},{"domain":"google.com","host":"","subdomain":"google.com","path":"","availability":"taken","register_url":"http://domai.nr/google.com/register"},{"domain":"google.net","host":"","subdomain":"google.net","path":"","availability":"taken","register_url":"http://domai.nr/google.net/register"},{"domain":"google.org","host":"","subdomain":"google.org","path":"","availability":"taken","register_url":"http://domai.nr/google.org/register"},{"domain":"google.co","host":"","subdomain":"google.co","path":"","availability":"taken","register_url":"http://domai.nr/google.co/register"},{"domain":"goo.gle","host":"","subdomain":"goo.gle","path":"","availability":"unavailable","register_url":"http://domai.nr/goo.gle/register"},{"domain":"goo.gl","host":"","subdomain":"goo.gl","path":"/e","availability":"unavailable","register_url":"http://domai.nr/goo.gl/register"},{"domain":"go.gle","host":"","subdomain":"go.gle","path":"","availability":"unavailable","register_url":"http://domai.nr/go.gle/register"},{"domain":"goog","host":"","subdomain":"goog","path":"/le","availability":"tld","register_url":"http://domai.nr/goog/register"},{"domain":"go.gl","host":"","subdomain":"go.gl","path":"/e","availability":"unavailable","register_url":"http://domai.nr/go.gl/register"},{"domain":"g.gle","host":"","subdomain":"g.gle","path":"","availability":"unavailable","register_url":"http://domai.nr/g.gle/register"},{"domain":"goo","host":"","subdomain":"goo","path":"/gle","availability":"tld","register_url":"http://domai.nr/goo/register"},{"domain":"g.gl","host":"","subdomain":"g.gl","path":"/e","availability":"unavailable","register_url":"http://domai.nr/g.gl/register"},{"domain":"gg","host":"","subdomain":"gg","path":"/le","availability":"tld","register_url":"http://domai.nr/gg/register"}]}'
parse_false_response = u'\x1b[31m\u2717\x1b[0m  google\n\x1b[31m\u2717\x1b[0m  google.com\n\x1b[31m\u2717\x1b[0m  google.net\n\x1b[31m\u2717\x1b[0m  google.org\n\x1b[31m\u2717\x1b[0m  google.co\n\x1b[31m\u2717\x1b[0m  goo.gle\n\x1b[31m\u2717\x1b[0m  goo.gl\n\x1b[31m\u2717\x1b[0m  go.gle\n\x1b[31m\u2717\x1b[0m  goog\n\x1b[31m\u2717\x1b[0m  go.gl\n\x1b[31m\u2717\x1b[0m  g.gle\n\x1b[31m\u2717\x1b[0m  goo\n\x1b[31m\u2717\x1b[0m  g.gl\n\x1b[31m\u2717\x1b[0m  gg'
info_data = {'domain': 'google', 'whois_url': 'http://domai.nr/google/whois', 'subregistration_permitted': False, 'register_url': 'http://domai.nr/google/register', 'tld': {'domain': 'google', 'wikipedia_url': 'http://domai.nr/google/wikipedia', 'iana_url': 'http://domai.nr/google/iana'}, 'registrars': [], 'subdomains': [], 'host': '', 'path': '', 'www_url': 'http://domai.nr/google/www', 'query': 'google', 'subdomain': 'google', 'domain_idna': 'google', 'availability': 'tld'}

class TestDomain(unittest.TestCase):


    def setUp(self):
        sys.argv = ['core.py','google']


    def tearDown(self):
        sys.argv = []


    def test_parse_info_false(self):
        domain = Domain()
        result = domain.parse(content, False)
        self.assertEquals(result, parse_false_response)


    def test_parse_info_true(self):
        domain = Domain()
        result = domain.parse(content, True)
        parse_true_response = json.loads(content)
        self.assertEquals(result, parse_true_response)


    def test_search_false(self):
        environment = Namespace(info=False, query=['google'])
        domain = Domain()
        result = domain.search(environment)
        self.assertEquals(result, parse_false_response)


    def test_search_true(self):
        environment = Namespace(info=True, query=['google'])
        domain = Domain()
        result = domain.search(environment)
        self.assertEquals(result, info_data)


    def test_flow(self):
        mock = MagicMock(spec=Domain)
        mock.main()
        mock.environment.assert_called_once()
        mock.search.assert_called_once()
        mock.parse.assert_called_once

if __name__ == '__main__':
    unittest.main()

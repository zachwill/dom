"""
Core functionality for Domainr.
"""

from argparse import ArgumentParser
import os
import requests
import simplejson as json
import sys
from termcolor import colored


class Domain(object):
    """Main class for interacting with the domains API."""

    def __init__(self):
        """Instantiate class, grab credentials from env if available"""
        if os.environ.get('DOMAINR_MASHAPE_KEY'):
            self.api_key = os.environ.get('DOMAINR_MASHAPE_KEY')
            self.api_key_name = 'mashape-key'
            self.api_endpoint = "https://domainr.p.mashape.com"
        elif os.environ.get('DOMAINR_CLIENT_ID'):
            self.api_key = os.environ.get('DOMAINR_CLIENT_ID')
            self.api_key_name = 'client_id'
            self.api_endpoint = "https://api.domainr.com"
        else:
            sys.exit("Error: No API key found in environment\n" +
                     "For more information, see README")

    @staticmethod
    def environment():
        """Parse any command line arguments."""
        parser = Domain._get_argparser()
        args = parser.parse_args()
        return args

    def search(self, env):
        """Use domainr to get information about domain names."""
        query = " ".join(env.query)
        params = {'query': query, self.api_key_name: self.api_key}

        url = self.api_endpoint + "/v2/search"

        json_data = requests.get(url, params=params)

        if not json_data.status_code == 200:
            return "Error: Status {0}; Response: {1}".format(json_data.status_code, json_data.content)
        data = self.parse_search(json_data.content, env)
        if not data:
            return "No results found\n"
        else:
            return data

    def status(self, env):
        """Use domainr to get information about domain names."""
        url = self.api_endpoint + "/v2/status"
        query = ",".join(env.query)
        json_data = requests.get(url, params={'domain': query, self.api_key_name: self.api_key})
        data = Domain.parse_status(json_data.content, env)
        return data

    @staticmethod
    def parse_search(content, env):
        """Parse the relevant data from JSON."""
        data = json.loads(content)
        results = data['results']
        if env.tld:
            output = [result['domain'] for result in results if Domain._tld_check(result['domain'])]
        else:
            output = [result['domain'] for result in results]
        output.sort()
        return output

    @staticmethod
    def parse_status(content, env):
        """Parse the relevant data from JSON."""
        data = json.loads(content)
        output = []
        status = data['status']
        for s in status:
            name = s['domain']
            status = s['status']
            if status.endswith('inactive'):
                name = colored(name, 'blue', attrs=['bold'])
                symbol = colored(u"\u2713", 'green')
                if env.ascii:
                    symbol = colored('A', 'green')
            else:
                # The available flag should skip these.
                if env.available:
                    continue
                symbol = colored(u"\u2717", 'red')
                if env.ascii:
                    symbol = colored('X', 'red')
            string = "%s  %s" % (symbol, name)
            output.append(string)
        output.sort()
        return output

    @staticmethod
    def _tld_check(name):
        """Make sure we're dealing with a top-level domain."""
        if name.endswith(".com") or name.endswith(".net") or name.endswith(".org"):
            return True
        return False

    @staticmethod
    def _get_argparser():
        """Helper function to get argument parser"""
        parser = ArgumentParser()
        parser.add_argument('query', type=str, nargs='+',
                            help="Your domain name query. With --no-suggest, must give full domain in query.")
        parser.add_argument('--ascii', action='store_true',
                            help="Use ASCII characters for domain availability.")
        parser.add_argument('--available', action='store_true',
                            help="Only show domain names that are currently available.")
        parser.add_argument('--tld', action='store_true',
                            help="Only check for top-level domains.")
        parser.add_argument('--no-suggest', action='store_true',
                            help="No suggested domains.")
        return parser

    def main(self):
        args = self.environment()
        if not args.no_suggest:
            args.query = self.search(args)
        status = self.status(args)
        print('\n'.join(status))


"""
Core functionality for Domainr.
"""

from argparse import ArgumentParser

import os
import requests
import simplejson as json
from termcolor import colored


mashape_key = os.getenv('MASHAPE_KEY')

class Domain(object):
    """Main class for interacting with the domains API."""

    def environment(self):
        """Parse any command line arguments."""
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
        args = parser.parse_args()
        return args

    def search(self, env):
        """Use domainr to get information about domain names."""
        url = "https://domainr.p.mashape.com/v2/search"
        query = env.query
        defaults = "club,co,im,ink,me,men,online,run,show,tech"
        location = "cn"
        registrar = "name.com"
        data = []
        for q in query:
            json_data = requests.get(url, params={'query': q, 'mashape-key': mashape_key,
                                                  'defaults': defaults, 'location': location, 'registrar': registrar})
            data.extend(self.parse_search(json_data.content, env))

        return data

    def status(self, env):
        """Use domainr to get information about domain names."""
        url = "https://domainr.p.mashape.com/v2/status"
        query = ",".join(env.query)
        json_data = requests.get(url, params={'domain': query, 'mashape-key': mashape_key})
        data = self.parse_status(json_data.content, env)
        return data

    def parse_search(self, content, env):
        """Parse the relevant data from JSON."""
        data = json.loads(content)
        results = data['results']
        if env.tld:
            output = [result['domain'] for result in results if self._tld_check(result['domain'])]
        else:
            output = [result['domain'] for result in results]
        output.sort()
        return output

    def parse_status(self, content, env):
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

    def _tld_check(self, name):
        """Make sure we're dealing with a top-level domain."""
        if name.endswith(".com") or name.endswith(".net") or name.endswith(".org"):
            return True
        return False

    def main(self):
        args = self.environment()
        if not args.no_suggest:
            args.query = self.search(args)
        status = self.status(args)
        print '\n'.join(status)


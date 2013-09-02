"""
Core functionality for Domainr.
"""

from argparse import ArgumentParser

import requests
import simplejson as json
from termcolor import colored


class Domain(object):
    """Main class for interacting with the domains API."""

    def environment(self):
        """Parse any command line arguments."""
        parser = ArgumentParser()
        parser.add_argument('query', type=str, nargs='+',
                            help="Your domain name query.")
        parser.add_argument('-i', '--info', action='store_true',
                            help="Get information for a domain name.")
        parser.add_argument('-a', '--ascii', action='store_true',
                            help="Use ASCII characters for domain availability.")
        args = parser.parse_args()
        return args

    def search(self, environment):
        """Use domainr to get information about domain names."""
        if environment.info:
            url = "http://domai.nr/api/json/info"
        else:
            url = "http://domai.nr/api/json/search"
        query = " ".join(environment.query)
        json_data = requests.get(url, params={'q': query})
        data = self.parse(json_data.content, environment)
        return data

    def parse(self, content, environment):
        """Parse the relevant data from JSON."""
        data = json.loads(content)
        if not environment.info:
            # Then we're dealing with a domain name search.
            output = []
            results = data['results']
            for domain in results:
                name = domain['domain']
                availability = domain['availability']
                if availability == 'available':
                    name = colored(name, 'blue', attrs=['bold'])
                    symbol = colored(u"\u2713", 'green')
                    if environment.ascii:
                        symbol = colored('A', 'green')
                else:
                    symbol = colored(u"\u2717", 'red')
                    if environment.ascii:
                        symbol = colored('X', 'red')
                string = "%s  %s" % (symbol, name)
                output.append(string)
            return '\n'.join(output)
        # Then the user wants information on a domain name.
        return data

    def main(self):
        args = self.environment()
        print self.search(args)

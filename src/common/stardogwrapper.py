#!/usr/bin/env python
import os
import requests
from subprocess import call, check_output
from rdflib import Graph

class StardogWrapper():
    def __init__(self, __config):
        '''
        Class constructor
        '''
        self.config = __config
        self.HOME_STARDOG = self.config.get('stardog', 'home_stardog')
        self.DB_NAME = self.config.get('stardog', 'db_name')
        self.DATA_PATH = self.config.get('io', 'data_path')
        self.RULE_FILE = self.config.get('io', 'rule_file')
        self.QB_FILE = self.config.get('io', 'qb_file')
        self.SL_QUERY = self.config.get('general', 'sl_query')
        self.REPORT_QUERY = self.config.get('general', 'report_query')
        self.INBOX_PATH = self.config.get('inbox', 'inbox_path')
        os.chdir(self.HOME_STARDOG)

    def removeLockFile(self):
        '''
        Removes Stardog lock file if server crashed
        '''
        if os.path.isfile(self.HOME_STARDOG + 'system.lock'):
            os.remove(self.HOME_STARDOG + 'system.lock')

    def stopServer(self):
        '''
        Stops Stardog server on the background
        '''
        # Clean knowledge base
        call([self.HOME_STARDOG + 'stardog-admin', 'db', 'drop', self.DB_NAME])
        # Attempt to shutdown the server
        call([self.HOME_STARDOG + 'stardog-admin', 'server', 'stop'])
        # In case a system.lock file remains, we delete it
        self.removeLockFile()

    def startServer(self):
        '''
        Starts Stardog on the background
        '''
        # In case a system.lock file remains, we delete it
        self.removeLockFile()
        # Attempt to start the server
        call([self.HOME_STARDOG + 'stardog-admin', 'server', 'start'])
        # Clean knowledge base
        call([self.HOME_STARDOG + 'stardog-admin', 'db', 'drop', self.DB_NAME])

    def restartServer(self):
        '''
        Restarts Stardog
        '''
        self.stopServer()
        self.startServer()

    def ingestRulesCubes(self):
        '''
        Ingest LER rules and cube into running instance from specified file
        '''
        call([self.HOME_STARDOG + 'stardog-admin', 'db', 'create', '-n',
              self.DB_NAME,
              self.DATA_PATH + self.QB_FILE,
              self.DATA_PATH + self.RULE_FILE])

    def query(self):
        '''
        Queries Stardog in SL reasoning mode
        '''
        # Trigger PROV and OA reporting through SPARQL INSERT using SL reasoning mode
        call([self.HOME_STARDOG + 'stardog', 'query', self.DB_NAME + ';reasoning=SL', self.SL_QUERY])
        # Query for the report graph, not in SL mode
        call([self.HOME_STARDOG + 'stardog', 'query', self.DB_NAME, self.REPORT_QUERY])
        #resp = Popen([self.HOME_STARDOG + 'stardog query ' + self.DB_NAME + ' ' + self.REPORT_QUERY], shell=True, stdout=PIPE)
        resp = check_output([self.HOME_STARDOG + 'stardog', 'query', self.DB_NAME, self.REPORT_QUERY])

        # If there is an LDN inbox defined, send the report graph there as a linked data notification
        if self.INBOX_PATH:
            # Discover inbox location
            r = requests.get(self.INBOX_PATH)
            inbox_url = ""
            try:
                inbox_url = r.links['http://www.w3.org/ns/ldp#inbox']['url']
            except:
                r = requests.get(self.INBOX_PATH, headers={'accept': 'text/turtle; q=1.0, application/ld+json; q=1.0'})
                g = Graph()
                try:
                    g.parse(r.text)
                    qres = g.query("select distinct ?inbox where {?foo <http://www.w3.org/ns/ldp#inbox> ?inbox . }")
                    for row in qres:
                        inbox_url = row
                except:
                    print "Could not discover LDN inbox in the specified URL"

            # Send the notification to the discovered inbox
            print 'Posting LER report graph notification to ' + inbox_url
            r = requests.post(inbox_url, resp, headers={'Content-Type': 'text/turtle'})
            print r.text


if __name__ == '__main__':
    s = StardogWrapper()
    s.restartServer()
    exit(0)

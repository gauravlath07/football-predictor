# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import urllib
from utilities.elasticsearch_interaction import ElasticSearchInteraction
from utilities.elasticsearch_schema import team_schema

config = SafeConfigParser()
config.read('utilities/config.ini')

# elastic search
# es_host = config.get('elasticsearch', 'HOST')
es_host = "35.166.200.54"
es_port = config.getint('elasticsearch', 'PORT')
es_index_name = config.get('elasticsearch', 'TEAM_INDEX')
es_doc_type = config.get('elasticsearch', 'TEAM_DOC_TYPE')
es = ElasticSearchInteraction(es_host, es_port)

# Read team data
teams_data_url = config.get('data_source', 'teams_data_url')
testfile = urllib.URLopener()
testfile.retrieve(teams_data_url, "teams.txt")
file = open('teams.txt', 'r')
obj = file.readlines()

es.create_index(es_index_name,team_schema)
es.index_team_content(es_index_name,es_doc_type,obj)

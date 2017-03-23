#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from utilities.elasticsearch_interaction import ElasticSearchInteraction
from utilities.team_data_processing import team_data_processing
import unicodedata
from utilities.elasticsearch_schema import process_schema
import sys
# sys.setdefaultencoding("utf-8")

config = SafeConfigParser()
config.read('utilities/config.ini')

# elastic search
es_host = config.get('elasticsearch', 'HOST')
es_port = config.getint('elasticsearch', 'PORT')
es_index_name = config.get('elasticsearch', 'PROCESS_INDEX')
es_doc_type = config.get('elasticsearch', 'PROCESS_DOC_TYPE')
es = ElasticSearchInteraction(es_host, es_port)

es.create_index(es_index_name,process_schema)

process = team_data_processing("localhost", "9200")
# process.process_features("Manchester United", "Chelsea")
process.get_team_names()
# data = u'naïve café'
# normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
# print process.strip_accents("Bellerín")

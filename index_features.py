#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from utilities.elasticsearch_interaction import ElasticSearchInteraction
from utilities.team_data_processing import team_data_processing
import unicodedata
from utilities.elasticsearch_schema import process_schema
import sys
# sys.setdefaultencoding("utf-8")

# config stuff
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
process.get_team_names()


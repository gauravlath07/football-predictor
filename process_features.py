import json
import urllib
from ConfigParser import SafeConfigParser
from utilities.elasticsearch_interaction import ElasticSearchInteractio
from utilities.team_data_processing import team_data_processing

config = SafeConfigParser()
config.read('utilities/config.ini')

# elastic search
es_host = config.get('elasticsearch', 'HOST')
es_port = config.getint('elasticsearch', 'PORT')
es_index_name = config.get('elasticsearch', 'INDEX')
es_doc_type = config.get('elasticsearch', 'DOC_TYPE')

team_data_processing.process_features("player_data", "Manchester United", "Chelsea")
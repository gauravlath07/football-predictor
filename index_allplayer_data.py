# noinspection PyPep8
import json
import urllib
from ConfigParser import SafeConfigParser
from utilities.elasticsearch_interaction import ElasticSearchInteraction

config = SafeConfigParser()
config.read('utilities/config.ini')

# elastic search
es_host = config.get('elasticsearch', 'HOST')
es_port = config.getint('elasticsearch', 'PORT')
es_index_name = config.get('elasticsearch', 'INDEX')
es_doc_type = config.get('elasticsearch', 'DOC_TYPE')
es = ElasticSearchInteraction(es_host, es_port)

# data sources
player_data_url = config.get('data_source', 'player_form_url')

es.create_index(es_index_name)
response = urllib.urlopen(player_data_url)
myfile = response.read()
data = json.loads(myfile)
#es.create_index(es_index_name)
es.index_content(es_index_name, es_doc_type, data)






from elasticsearch import Elasticsearch
#from elasticsearch_schema import schema
#from elasticsearch_schema import blacklist_schema
from ConfigParser import SafeConfigParser
#from logger import Logger

import datetime


class ElasticSearchInteraction:
    def __init__(self, host, port, indexName, docType):
        self.es = Elasticsearch([{'host': host, 'port': port}])
        self.index_name = indexName
        self.doc_type = docType
        self.blacklist_index_name = blacklistIndexName
        self.blacklist_doc_type = blacklistDocType

    def create_index(self):

        if not self.es.indices.exists(self.index_name):
            self.es.indices.create(self.index_name, schema)

    def index_content(self, website_url, alchemy_data, feed):

        dictionary = {}
        #clean data

        self.es.index(index=self.index_name, doc_type=self.doc_type, body=dictionary)
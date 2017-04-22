from elasticsearch import Elasticsearch
from logger import Logger
from JSONSerializer import JSONSerializer
import json 

import datetime


class ElasticSearchInteraction:
    def __init__(self, host, port):
        self.es = Elasticsearch([{'host': host, 'port': port}],serializer=JSONSerializer())
        logger = Logger('ElasticSearchInteraction.log')

    def url_exists(self, URL, index_name):
        res = self.es.search(index=index_name, body={"query": {"match": {"url": URL}}})
        if res['hits']['total'] > 0:
            return True
        else:
            return False

    def title_exists(self, title, index_name):
        res = self.es.search(index=index_name, body={"query": {"match_phrase": {"title": title}}})
        if res['hits']['total'] > 0:
            return True
        else:
            return False

    def create_index(self, index_name, index_schema,blacklist_index_name,blacklist_schema):

        if not self.es.indices.exists(index_name):
            self.es.indices.create(index_name, index_schema)

        if not self.es.indices.exists(blacklist_index_name):
            self.es.indices.create(blacklist_index_name, blacklist_schema)

    def index_content(self, index_name, doc_type, dictionary):
        self.es.index(index=index_name, doc_type=doc_type, body=dictionary)

    def blacklist_url(self, website_url, feed, index_name, doc_type):
        dictionary = {}
        dictionary['rss_source'] = feed
        dictionary['url'] = website_url
        self.es.index(index=index_name, doc_type=doc_type, body=dictionary)

    def check_if_blacklisted(self, website_url, index_name):
        res = self.es.search(index=index_name, body={"query": {"match": {"url": website_url}}})
        hits = res['hits']['total']
        if hits > 0:
            return True
            
     
    def es_search(self, _index, _body, _size=5000, _returnfields=['_all'], _searchfields=['_all'],
    _minimum_should_match=1,_sort=[],_aggs={},_highlight={},_timeframe={}):
        res = self.es.search(
            index=_index,
            size=_size,
            body=_body
        )
        return res
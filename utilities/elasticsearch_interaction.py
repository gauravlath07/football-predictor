# noinspection PyPep8
from elasticsearch import Elasticsearch
from elasticsearch_schema import schema
#from elasticsearch_schema import blacklist_schema
from ConfigParser import SafeConfigParser
#from logger import Logger

import datetime
import csv


class ElasticSearchInteraction:
    def __init__(self, host, port):
        self.es = Elasticsearch([{'host': host, 'port': port}])
        self.team_code_dict = {}

        with open('team_codes.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.team_code_dict[row['team_code']] = row['team_name']

    def create_index(self, index_name):

        if not self.es.indices.exists(index_name):
            self.es.indices.create(index_name, schema)

    def index_content(self, index_name, doc_type, player_data):

        dictionary = {}
        dictionary['latest_player_data'] = []

        for player in player_data:
            temp = {}
            temp['web_name'] = player['web_name']
            temp['team'] = self.get_team_name(str(player['team']))
            temp['first_name'] = player['first_name']
            temp['last_name'] = player['second_name']
            temp['fantasy_cost_change'] = float(player['cost_change_start'])
            temp['in_dreamteam'] = bool(player['in_dreamteam'])
            temp['dreamteam_count'] = float(player['dreamteam_count'])
            temp['selected_percentage'] = float(player['selected_by_percent'])
            temp['form'] = float(player['form'])
            temp['fantasy_transfers_out_in'] = float(player['transfers_out']) - float(player['transfers_in'])
            temp['fantasy_total_points'] = float(player['total_points'])
            temp['fantasy_points_per_game'] = float(player['points_per_game'])
            temp['minutes_played'] = float(player['minutes'])
            temp['goals_scored"'] = float(player['goals_scored'])
            temp['assists'] = float(player['assists'])
            temp['yellow_cards'] = float(player['yellow_cards'])
            temp['red_cards'] = float(player['red_cards'])
            temp['influence'] = float(player['influence'])
            temp['creativity'] = float(player['creativity'])
            temp['threat'] = float(player['threat'])
            temp['ict_index'] = float(player['ict_index'])
            temp['ea_index'] = float(player['ea_index'])
            dictionary['latest_player_data'].append(temp)
            print "added " + player['web_name'] + " to dictionary"

        dictionary['date_indexed'] = datetime.datetime.today()

        self.es.index(index=index_name, doc_type=doc_type, body=dictionary)
        print "indexeing successful !! "

    def get_team_name(self, team_code):
        return self.team_code_dict[team_code]


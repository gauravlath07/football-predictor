# noinspection PyPep8
from elasticsearch import Elasticsearch
import re
from HTMLParser import HTMLParser
#from elasticsearch_schema import blacklist_schema
from ConfigParser import SafeConfigParser
#from logger import Logger

import datetime
import csv


class ElasticSearchInteraction:
    def __init__(self, host, port):
        self.es = Elasticsearch([{'host': host, 'port': port}])
        self.team_code_dict = {}

        with open('utilities/team_codes.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.team_code_dict[row['team_code']] = row['team_name']

    def create_index(self, index_name, schema):

        if not self.es.indices.exists(index_name):
            self.es.indices.create(index_name, schema)

    def index_player_content(self, index_name, doc_type, player_data):

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
            temp['goals_scored'] = float(player['goals_scored'])
            temp['assists'] = float(player['assists'])
            temp['bonus'] = float(player['bonus'])
            temp['yellow_cards'] = float(player['yellow_cards'])
            temp['red_cards'] = float(player['red_cards'])
            temp['influence'] = float(player['influence'])
            temp['creativity'] = float(player['creativity'])
            temp['threat'] = float(player['threat'])
            temp['ict_index'] = float(player['ict_index'])
            temp['ea_index'] = float(player['ea_index'])
            temp['icon_link'] = self.make_icon_link(temp['team'])
            dictionary['latest_player_data'].append(temp)
            print "added " + player['web_name'] + " to dictionary"

        dictionary['date_indexed'] = datetime.datetime.today()

        self.es.index(index=index_name, doc_type=doc_type, body=dictionary)
        print "indexeing successful !! "

    def get_team_name(self, team_code):
        return self.team_code_dict[team_code]

    def make_icon_link(self, team_name):
        string_name = "icons/"+team_name.replace(" ","")+".png"
        return string_name

    def index_team_content(self, index_name, doc_type, team_data):
        team_index = 11
        dictionary = {}
        dictionary['latest_team_data'] = []

        while team_index < 202:
            temp = {}
            temp_float = re.sub('<[^<]+?>', '', team_data[team_index]).strip()
            temp['team_name'] = temp_float
            temp_float = re.sub('<[^<]+?>', '', team_data[team_index + 3])
            temp['total_shot_ratio'] = float(temp_float)
            temp_float = re.sub('<[^<]+?>', '', team_data[team_index + 4])
            temp['shots_on_target'] = float(temp_float)
            temp_float = re.sub('<[^<]+?>', '', team_data[team_index + 5])
            temp['shoot_percentage'] = float(temp_float)
            temp_float = re.sub('<[^<]+?>', '', team_data[team_index + 6])
            temp['save_percentage'] = float(temp_float)
            temp_float = re.sub('<[^<]+?>', '', team_data[team_index + 7])
            temp['pdo'] = float(temp_float)
            dictionary['latest_team_data'].append(temp)
            print "added " + team_data[team_index]
            team_index += 10

        dictionary['date_indexed'] = datetime.datetime.today()
        self.es.index(index=index_name, doc_type=doc_type, body=dictionary)
        print "all done"

    def index_features(self, index_name, doc_type, features_data):
        self.es.index(index=index_name, doc_type=doc_type, body=features_data)



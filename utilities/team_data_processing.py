#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from elasticsearch import Elasticsearch
import csv
from sklearn import preprocessing
import unicodedata
from utilities.elasticsearch_interaction import ElasticSearchInteraction
import datetime
from utilities.elasticsearch_schema import process_schema

class team_data_processing:

    def __init__(self,host,port):
        print "team data processing is running"
        self.es = Elasticsearch([{'host': host, 'port': port}])
        self.main_11 = {}
        self.get_main_11()
        self.es_inter = ElasticSearchInteraction(host, port)

    def get_team_names(self):
        with open("utilities/latest-matchday.txt") as f:
            content = [x.strip('\n') for x in f.readlines()]
        # you may also want to remove whitespace characters like `\n` at the end of each line
        for item in content:
            m = re.search("\d", item)
            if m:
                score_position = m.start()
                home_position = score_position-1
                home_team = item[:home_position].strip()
                temp_string = item[home_position:]
                n = re.search("[A-Z]", temp_string)
                away_position = n.start()
                away_team = temp_string[away_position:]
                score = float(item[score_position:score_position+1])-float(item[score_position+2:score_position+3])
            else:
                print "Match hasnt taken place yet"
            # print home_team
            # print away_team
            # print score
            self.process_features(home_team, away_team, score)

    def get_main_11(self):
        with open('utilities/main-11.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.main_11[row['team_name']] = row['players'].strip()

    def process_features(self, home_team, away_team, score):
        player_res = self.es.search(index="player_data", body={"sort": [{"date_indexed": {"order": "desc"}}], "query": {"match_all" : {}},"size" : 1})
        player_data = player_res['hits']['hits'][0]['_source']['latest_player_data']

        team_res = self.es.search(index="team_data", body={"sort": [{"date_indexed": {"order": "desc"}}], "query": {"match_all" : {}},"size" : 1})
        team_data = team_res['hits']['hits'][0]['_source']['latest_team_data']
        for item in team_data:
            if item['team_name'] == "Man City":
                item['team_name'] = "Manchester City"
            elif item['team_name'] == "Man United":
                item['team_name'] = "Manchester United"
            elif item['team_name'] == "West Brom":
                item['team_name'] = "West Bromwich Albion"
            elif item['team_name'] == "Stoke":
                item['team_name'] = "Stoke City"
            elif item['team_name'] == "Swansea":
                item['team_name'] = "Swansea City"
            elif item['team_name'] == "Leicester":
                item['team_name'] = "Leicester City"
            elif item['team_name'] == "Swansea":
                item['team_name'] = "Swansea City"
            elif item['team_name'] == "Hull":
                item['team_name'] = "Hull City"
            elif item['team_name'] == "Swansea":
                item['team_name'] = "Swansea City"
            elif item['team_name'] == "Bournemouth":
                item['team_name'] = "AFC Bournemouth"

        home_team_data = filter(lambda team_name: team_name['team_name'] == home_team, team_data)
        home_team_data = home_team_data[0]
        away_team_data = filter(lambda team_name: team_name['team_name'] == away_team, team_data)
        away_team_data = away_team_data[0]
        # print home_team_data

        home_team_main11_data = []
        away_team_main11_data = []

        temp_home = self.main_11[home_team]
        home_team_main11 = temp_home.split(";")
        temp_away = self.main_11[away_team]
        away_team_main11 = temp_away.split(";")
        for item in player_data:
            temp_obj = item['web_name']
            item['web_name'] = self.strip_accents(temp_obj)
        # for item in player_data:
        #     print item['web_name']
        #     print type(item['web_name'])

        for item in home_team_main11:
            temp_object = filter(lambda player: player['web_name'] == item, player_data)
            individual_player_data = filter(lambda player: player['team'] == home_team, temp_object)
            print item
            temp = individual_player_data[0]
            home_team_main11_data.append(temp)
        for item in away_team_main11:
            temp_object = filter(lambda player: player['web_name'] == item, player_data)
            individual_player_data = filter(lambda player: player['team'] == away_team, temp_object)
            print item
            temp = individual_player_data[0]
            away_team_main11_data.append(temp)

        # for item in home_team_main11_data:
        #     print item
        # for item in away_team_main11_data:
        #     print item

        dictionary = {}
        dictionary['home_team_name'] = home_team
        dictionary['away_team_name'] = away_team
        dictionary['score'] = score
        dictionary['fantasy_cost_change'] = self.avg_and_minus("fantasy_cost_change", home_team_main11_data, away_team_main11_data)
        # dictionary['in_dreamteam'] =
        dictionary['dreamteam_count'] = self.avg_and_minus("dreamteam_count", home_team_main11_data, away_team_main11_data)
        dictionary['selected_percentage'] = self.avg_and_minus("selected_percentage", home_team_main11_data, away_team_main11_data)
        dictionary['form'] = self.avg_and_minus("form", home_team_main11_data, away_team_main11_data)
        dictionary['fantasy_transfers_out_in'] = self.avg_and_minus("fantasy_transfers_out_in", home_team_main11_data, away_team_main11_data)
        dictionary['fantasy_total_points'] = self.avg_and_minus("fantasy_points_per_game", home_team_main11_data, away_team_main11_data)
        dictionary['fantasy_points_per_game'] = self.avg_and_minus("fantasy_points_per_game",home_team_main11_data, away_team_main11_data)
        dictionary['minutes_played'] = self.avg_and_minus("minutes_played", home_team_main11_data, away_team_main11_data)
        dictionary['goals_scored'] = self.avg_and_minus("goals_scored", home_team_main11_data, away_team_main11_data)
        dictionary['assists'] = self.avg_and_minus("assists", home_team_main11_data, away_team_main11_data)
        dictionary['yellow_cards'] = self.avg_and_minus("yellow_cards",home_team_main11_data, away_team_main11_data)
        dictionary['red_cards'] = self.avg_and_minus("red_cards",home_team_main11_data, away_team_main11_data)
        dictionary['bonus'] = self.avg_and_minus("bonus",home_team_main11_data, away_team_main11_data)
        dictionary['influence'] = self.avg_and_minus("influence",home_team_main11_data, away_team_main11_data)
        dictionary['creativity'] = self.avg_and_minus("creativity",home_team_main11_data, away_team_main11_data)
        dictionary['threat'] = self.avg_and_minus("threat",home_team_main11_data, away_team_main11_data)
        dictionary['ict_index'] = self.avg_and_minus("ict_index",home_team_main11_data, away_team_main11_data)
        dictionary['ea_index'] = self.avg_and_minus("ea_index",home_team_main11_data, away_team_main11_data)
        dictionary['total_shot_ratio'] = float(home_team_data['total_shot_ratio']) - float(away_team_data['total_shot_ratio'])
        dictionary['shots_on_target'] = float(home_team_data['total_shot_ratio']) - float(away_team_data['total_shot_ratio'])
        dictionary['shoot_percentage'] = float(home_team_data['total_shot_ratio']) - float(away_team_data['total_shot_ratio'])
        dictionary['save_percentage'] = float(home_team_data['total_shot_ratio']) - float(away_team_data['total_shot_ratio'])
        dictionary['pdo'] = float(home_team_data['total_shot_ratio']) - float(away_team_data['total_shot_ratio'])
        dictionary['date_indexed'] = datetime.datetime.today()

        self.es_inter.index_features("data_features", "match_data", dictionary)
        print "indexed" + home_team + " vs " + away_team



    def normalize_data(self, array):
        normalized_array = preprocessing.normalize(array)
        return normalized_array

    def strip_accents(self, s):
        # obj = s.decode('utf-8')
        obj = ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')
        obj = unicodedata.normalize('NFKD', obj).encode('ascii','ignore')
        return obj

    def avg_and_minus(self, tag, home_data, away_data):
        home_obj = sum(d[tag] for d in home_data) / len(home_data)
        away_obj = sum(d[tag] for d in away_data) / len(away_data)
        return home_obj-away_obj







# coding=utf-8
import csv
from ConfigParser import SafeConfigParser
from api.indexing.utilities.elasticsearch_interaction import ElasticSearchInteraction
from api.indexing.utilities.team_data_processing import team_data_processing
from api.indexing.utilities.elasticsearch_schema import player_schema
from elasticsearch import Elasticsearch

es_host = "35.166.200.54"
es_port = "9200"
es_index_name = "team_data"
es_doc_type = "team_stats"
es = Elasticsearch([{'host': es_host, 'port': es_port}])
# es.indices.create(es_index_name, player_schema)
first = True

dictionary = { "latest_team_data": [ { "total_shot_ratio": 63.85,"pdo": 112.88,"save_percentage": 71.62,"shoot_percentage": 41.26,"shots_on_target": 65.9,"team_name": "Chelsea"},{ "total_shot_ratio": 65.18,"pdo": 107.54,"save_percentage": 75,"shoot_percentage": 32.54,"shots_on_target": 66.8,"team_name": "Tottenham"},{ "total_shot_ratio": 66.22,"pdo": 98.76,"save_percentage": 62.03,"shoot_percentage": 36.73,"shots_on_target": 65.04,"team_name": "Man City"},{ "total_shot_ratio": 67.27,"pdo": 94.71,"save_percentage": 60.44,"shoot_percentage": 34.27,"shots_on_target": 66.17,"team_name": "Liverpool"},{ "total_shot_ratio": 65.3,"pdo": 94.84,"save_percentage": 70.13,"shoot_percentage": 24.71,"shots_on_target": 68.83,"team_name": "Man United"},{ "total_shot_ratio": 58.25,"pdo": 111.31,"save_percentage": 70.43,"shoot_percentage": 40.88,"shots_on_target": 54.37,"team_name": "Arsenal"},{ "total_shot_ratio": 53.11,"pdo": 105.47,"save_percentage": 71.7,"shoot_percentage": 33.77,"shots_on_target": 58.75,"team_name": "Everton"},{ "total_shot_ratio": 43.6,"pdo": 111.39,"save_percentage": 70.77,"shoot_percentage": 40.63,"shots_on_target": 42.48,"team_name": "West Brom"},{ "total_shot_ratio": 42.51,"pdo": 99.9,"save_percentage": 69.34,"shoot_percentage": 30.56,"shots_on_target": 44.08,"team_name": "Stoke"},{ "total_shot_ratio": 59.21,"pdo": 81.23,"save_percentage": 57.14,"shoot_percentage": 24.09,"shots_on_target": 61.99,"team_name": "Southampton"},{ "total_shot_ratio": 45.15,"pdo": 95.3,"save_percentage": 61.43,"shoot_percentage": 33.87,"shots_on_target": 46.97,"team_name": "Bournemouth"},{ "total_shot_ratio": 50.32,"pdo": 102.35,"save_percentage": 63.89,"shoot_percentage": 38.46,"shots_on_target": 41.94,"team_name": "West Ham"},{ "total_shot_ratio": 36.19,"pdo": 106.99,"save_percentage": 74.7,"shoot_percentage": 32.29,"shots_on_target": 36.64,"team_name": "Burnley"},{ "total_shot_ratio": 43.27,"pdo": 95.91,"save_percentage": 64.18,"shoot_percentage": 31.73,"shots_on_target": 43.7,"team_name": "Watford"},{ "total_shot_ratio": 43.39,"pdo": 99.62,"save_percentage": 65.94,"shoot_percentage": 33.67,"shots_on_target": 41.53,"team_name": "Leicester"},{ "total_shot_ratio": 47.41,"pdo": 98.58,"save_percentage": 64.62,"shoot_percentage": 33.96,"shots_on_target": 44.92,"team_name": "Crystal Palace"},{ "total_shot_ratio": 43.2,"pdo": 86.45,"save_percentage": 55.94,"shoot_percentage": 30.51,"shots_on_target": 45.21,"team_name": "Swansea"},{ "total_shot_ratio": 37.97,"pdo": 91.42,"save_percentage": 65.68,"shoot_percentage": 25.74,"shots_on_target": 37.41,"team_name": "Hull"},{ "total_shot_ratio": 39.75,"pdo": 101.68,"save_percentage": 72.27,"shoot_percentage": 29.41,"shots_on_target": 36.36,"team_name": "Middlesbrough"},{ "total_shot_ratio": 35.14,"pdo": 100.64,"save_percentage": 72.07,"shoot_percentage": 28.57,"shots_on_target": 31.94,"team_name": "Sunderland"}]}

es.index(index=es_index_name, doc_type=es_doc_type, body=dictionary)
        # print row + "done"

# with open('features.csv') as f:
#     dict = {}
#     reader = csv.reader(f)
#     for row in reader:
#         print row
#         if first == True:
#             first = False
#             continue
#         dictionary = {}
#         dictionary['home_team_name'] = row[14]
#         dictionary['away_team_name'] = row[11]
#         dictionary['score'] = row[17]
#         dictionary['home'] = row[33]
#         dictionary['away'] = row[32]
#         dictionary['fantasy_cost_change'] = row[8]
#         dictionary['in_dreamteam'] = row[13]
#         dictionary['dreamteam_count'] = row[26]
#         dictionary['selected_percentage'] = row[10]
#         dictionary['form'] = row[21]
#         dictionary['fantasy_transfers_out_in'] = row[25]
#         dictionary['fantasy_total_points'] = row[20]
#         dictionary['fantasy_points_per_game'] = row[6]
#         dictionary['minutes_played'] = row[15]
#         dictionary['goals_scored'] = row[31]
#         dictionary['assists'] = row[23]
#         dictionary['yellow_cards'] = row[4]
#         dictionary['red_cards'] = row[30]
#         dictionary['bonus'] = row[22]
#         dictionary['influence'] = row[6]
#         dictionary['creativity'] = row[16]
#         dictionary['threat'] = row[29]
#         dictionary['ict_index'] = row[18]
#         dictionary['ea_index'] = row[24]
#         dictionary['total_shot_ratio'] = row[5]
#         dictionary['shots_on_target'] = row[12]
#         dictionary['shoot_percentage'] = row[9]
#         dictionary['save_percentage'] = row[27]
#         dictionary['pdo'] = row[28]
#         dictionary['date_indexed'] = row[19]
#         print dictionary
#         es.index(index=es_index_name, doc_type=es_doc_type, body=dictionary)
#         # print row + "done"

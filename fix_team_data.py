from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': "9200"}])
# 0dic =  {
# "latest_team_data": [
# {
# "total_shot_ratio": 63.32,
# "pdo": 110.67,
# "save_percentage": 71.43,
# "shoot_percentage": 39.24,
# "shots_on_target": 65.29,
# "team_name": "Chelsea"
# }
# ,
# {
# "total_shot_ratio": 65.4,
# "pdo": 107.32,
# "save_percentage": 74.71,
# "shoot_percentage": 32.61,
# "shots_on_target": 67.9,
# "team_name": "Tottenham"
# }
# ,
# {
# "total_shot_ratio": 67.14,
# "pdo": 94.17,
# "save_percentage": 59.79,
# "shoot_percentage": 34.38,
# "shots_on_target": 66.44,
# "team_name": "Liverpool"
# }
# ,
# {
# "total_shot_ratio": 66.01,
# "pdo": 96.31,
# "save_percentage": 60.47,
# "shoot_percentage": 35.85,
# "shots_on_target": 64.9,
# "team_name": "Man City"
# }
# ,
# {
# "total_shot_ratio": 58.23,
# "pdo": 111.71,
# "save_percentage": 70.49,
# "shoot_percentage": 41.22,
# "shots_on_target": 54.81,
# "team_name": "Arsenal"
# }
# ,
# {
# "total_shot_ratio": 65.74,
# "pdo": 95.16,
# "save_percentage": 70.73,
# "shoot_percentage": 24.43,
# "shots_on_target": 68.22,
# "team_name": "Man United"
# }
# ,
# {
# "total_shot_ratio": 52.38,
# "pdo": 103.77,
# "save_percentage": 70.43,
# "shoot_percentage": 33.33,
# "shots_on_target": 58.03,
# "team_name": "Everton"
# }
# ,
# {
# "total_shot_ratio": 43.61,
# "pdo": 109.76,
# "save_percentage": 70.37,
# "shoot_percentage": 39.39,
# "shots_on_target": 42.31,
# "team_name": "West Brom"
# }
# ,
# {
# "total_shot_ratio": 59.04,
# "pdo": 82.89,
# "save_percentage": 58.89,
# "shoot_percentage": 24,
# "shots_on_target": 62.5,
# "team_name": "Southampton"
# }
# ,
# {
# "total_shot_ratio": 44.02,
# "pdo": 96.5,
# "save_percentage": 65.47,
# "shoot_percentage": 31.03,
# "shots_on_target": 45.49,
# "team_name": "Watford"
# }
# ,
# {
# "total_shot_ratio": 45.04,
# "pdo": 99.03,
# "save_percentage": 67.13,
# "shoot_percentage": 31.9,
# "shots_on_target": 44.79,
# "team_name": "Leicester"
# }
# ,
# {
# "total_shot_ratio": 42.71,
# "pdo": 99.46,
# "save_percentage": 70,
# "shoot_percentage": 29.46,
# "shots_on_target": 42.75,
# "team_name": "Stoke"
# }
# ,
# {
# "total_shot_ratio": 44.53,
# "pdo": 97.27,
# "save_percentage": 63.16,
# "shoot_percentage": 34.11,
# "shots_on_target": 45.91,
# "team_name": "Bournemouth"
# }
# ,
# {
# "total_shot_ratio": 36.24,
# "pdo": 106.54,
# "save_percentage": 74.86,
# "shoot_percentage": 31.68,
# "shots_on_target": 36.59,
# "team_name": "Burnley"
# }
# ,
# {
# "total_shot_ratio": 49.76,
# "pdo": 100.5,
# "save_percentage": 63.23,
# "shoot_percentage": 37.27,
# "shots_on_target": 41.51,
# "team_name": "West Ham"
# }
# ,
# {
# "total_shot_ratio": 46.1,
# "pdo": 101.49,
# "save_percentage": 66.67,
# "shoot_percentage": 34.82,
# "shots_on_target": 42.75,
# "team_name": "Crystal Palace"
# }
# ,
# {
# "total_shot_ratio": 38.66,
# "pdo": 94.89,
# "save_percentage": 65.54,
# "shoot_percentage": 29.36,
# "shots_on_target": 38.11,
# "team_name": "Hull"
# }
# ,
# {
# "total_shot_ratio": 43.14,
# "pdo": 86.91,
# "save_percentage": 56.58,
# "shoot_percentage": 30.33,
# "shots_on_target": 44.53,
# "team_name": "Swansea"
# }
# ,
# {
# "total_shot_ratio": 39.65,
# "pdo": 101,
# "save_percentage": 70.87,
# "shoot_percentage": 30.14,
# "shots_on_target": 36.5,
# "team_name": "Middlesbrough"
# }
# ,
# {
# "total_shot_ratio": 35.38,
# "pdo": 99.76,
# "save_percentage": 73.1,
# "shoot_percentage": 26.67,
# "shots_on_target": 31.36,
# "team_name": "Sunderland"
# }
# ]}
# home_pdo = 81.23
# home_save_percentage = 57.14
# home_shoot_percentage = -30.16
# home_total_shot_ratio = 0
# home_shots_on_target = 0
#
# away_pdo = 81.23
# away_save_percentage = 57.14
# away_shoot_percentage = -30.16
# away_total_shot_ratio = 0
# away_shots_on_target =

# home_team = "West Brom"
# away_team = "Southampton"
#
# for item in dic['latest_team_data']:
#     if item['team_name'] == home_team:
#         home_pdo = item['pdo']
#         home_save_percentage = item['save_percentage']
#         home_shoot_percentage = item['shoot_percentage']
#         home_total_shot_ratio = item['total_shot_ratio']
#         home_shots_on_target = item['shots_on_target']
#     if item['team_name'] == away_team:
#         away_pdo = item['pdo']
#         away_save_percentage = item['save_percentage']
#         away_shoot_percentage = item['shoot_percentage']
#         away_total_shot_ratio = item['total_shot_ratio']
#         away_shots_on_target = item['shots_on_target']
#
# pdo = home_pdo-away_pdo
# save_percentage = home_save_percentage-away_save_percentage
# shoot_percentage = home_shoot_percentage-away_shoot_percentage
# total_shot_ratio = home_total_shot_ratio-away_total_shot_ratio
# shots_on_target = home_shots_on_target-away_shots_on_target
#
id = "AVt-T9cvhGAJAgpMbR-P"
home = 2
away = 2
es.update(index='data_features', doc_type='match_data', id=id, body={"doc": {"home": home, "away": away}})
# es.delete(index='data_features', doc_type='match_data',id=id)
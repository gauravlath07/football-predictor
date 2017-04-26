# coding=utf-8
from ConfigParser import SafeConfigParser
from elasticsearch import Elasticsearch
from ConfigParser import SafeConfigParser
from utilities.team_data_processing import team_data_processing
from sklearn.ensemble import RandomForestClassifier
import pandas as pd



class predict:

    def __init__(self):
        # config stuff
        config = SafeConfigParser()
        config.read('indexing/utilities/config.ini')

        es_host = config.get('elasticsearch', 'HOST')
        es_port = config.getint('elasticsearch', 'PORT')
        es_index_name = config.get('elasticsearch', 'PROCESS_INDEX')
        es_doc_type = config.get('elasticsearch', 'PROCESS_DOC_TYPE')
        es = Elasticsearch([{'host': es_host, 'port': es_port}])

        # es_host = "localhost"
        # es_port = "9200"
        # es_index_name = "data_features"
        # es = Elasticsearch([{'host': es_host, 'port': es_port}])

        res = es.search(index=es_index_name, body={"size": 100, "query": {"match_all": {}}})
        res = res['hits']['hits']

        yellow_cards = []
        total_shot_ratio = []
        fantasy_points_per_game = []
        influence = []
        fantasy_cost_change = []
        shoot_percentage = []
        selected_percentage = []
        shots_on_target = []
        in_dreamteam = []
        minutes_played = []
        creativity = []
        ict_index = []
        fantasy_total_points = []
        form = []
        bonus = []
        assists = []
        ea_index = []
        fantasy_transfers_out_in = []
        dreamteam_count = []
        save_percentage = []
        pdo = []
        threat = []
        red_cards = []
        goals_scored = []
        home = []
        away = []
        score = []

        for item in res:
            yellow_cards.append(item['_source']['yellow_cards'])
            total_shot_ratio.append(item['_source']['total_shot_ratio'])
            fantasy_points_per_game.append(item['_source']['fantasy_points_per_game'])
            influence.append(item['_source']['influence'])
            fantasy_cost_change.append(item['_source']['fantasy_cost_change'])
            shoot_percentage.append(item['_source']['shoot_percentage'])
            selected_percentage.append(item['_source']['selected_percentage'])
            shots_on_target.append(item['_source']['shots_on_target'])
            in_dreamteam.append(item['_source']['in_dreamteam'])
            minutes_played.append(item['_source']['minutes_played'])
            creativity.append(item['_source']['creativity'])
            ict_index.append(item['_source']['ict_index'])
            fantasy_total_points.append(item['_source']['fantasy_total_points'])
            form.append(item['_source']['form'])
            bonus.append(item['_source']['bonus'])
            assists.append(item['_source']['assists'])
            ea_index.append(item['_source']['ea_index'])
            fantasy_transfers_out_in.append(item['_source']['fantasy_transfers_out_in'])
            dreamteam_count.append(item['_source']['dreamteam_count'])
            save_percentage.append(item['_source']['save_percentage'])
            pdo.append(item['_source']['pdo'])
            threat.append(item['_source']['threat'])
            red_cards.append(item['_source']['red_cards'])
            goals_scored.append(item['_source']['goals_scored'])
            home.append(item['_source']['home'])
            away.append(item['_source']['away'])
            score.append(item['_source']['score'])
        d = {'yellow_cards': yellow_cards,
             'total_shot_ratio': total_shot_ratio,
             'fantasy_points_per_game': fantasy_points_per_game,
             'influence': influence,
             'fantasy_cost_change': fantasy_cost_change,
             'shoot_percentage': shoot_percentage,
             'selected_percentage': selected_percentage,
             'shots_on_target': shots_on_target,
             'in_dreamteam': in_dreamteam,
             'minutes_played': minutes_played,
             'ict_index': ict_index,
             'fantasy_total_points': fantasy_total_points,
             'form': form,
             'bonus': bonus,
             'assists': assists,
             'ea_index': ea_index,
             'fantasy_transfers_out_in': fantasy_transfers_out_in,
             'dreamteam_count': dreamteam_count,
            'save_percentage': save_percentage,
            'pdo': pdo,
            'threat': threat,
            'red_cards': red_cards,
            'goals_scored': goals_scored,
             'home': home,
             'away': away,
            'score': score}

        self.df = pd.DataFrame(d)
        # self.df.loc[self.df["score"] > 0, "score"] = 1
        # self.df.loc[self.df["score"] == 0, "score"] = 0
        # self.df.loc[self.df["score"] < 0, "score"] = -1
        # print self.df

        self.predictors = ["form","assists","pdo", "shots_on_target","total_shot_ratio","fantasy_points_per_game",
                           "influence", "ict_index",  "form", "ea_index", "threat", "goals_scored",
                           "fantasy_cost_change", "shoot_percentage","fantasy_total_points" ]
        self.alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=7, min_samples_leaf=3)
        print "changed"

        self.process = team_data_processing(es_host, es_port)

    def process_new_feature(self, json_doc):

        return_doc = self.process.get_features(json_doc)
        d_predict = {'yellow_cards': [return_doc["yellow_cards"]],
             'total_shot_ratio': [return_doc["total_shot_ratio"]],
             'fantasy_points_per_game': [return_doc["fantasy_points_per_game"]],
             'influence': [return_doc["influence"]],
             'fantasy_cost_change': [return_doc["fantasy_cost_change"]],
             'shoot_percentage': [return_doc["shoot_percentage"]],
             'selected_percentage': [return_doc["selected_percentage"]],
             'shots_on_target': [return_doc["shots_on_target"]],
             'in_dreamteam': [return_doc["in_dreamteam"]],
             'minutes_played': [return_doc["minutes_played"]],
             'ict_index': [return_doc["ict_index"]],
             'fantasy_total_points': [return_doc["fantasy_total_points"]],
             'form': [return_doc["form"]],
             'bonus': [return_doc["bonus"]],
             'assists': [return_doc["assists"]],
             'ea_index': [return_doc["ea_index"]],
             'fantasy_transfers_out_in': [return_doc["fantasy_transfers_out_in"]],
             'dreamteam_count': [return_doc["dreamteam_count"]],
            'save_percentage': [return_doc["save_percentage"]],
            'pdo': [return_doc["pdo"]],
            'threat': [return_doc["threat"]],
            'red_cards': [return_doc["red_cards"]],
            'goals_scored': [return_doc["goals_scored"]]}

        df_predict = pd.DataFrame(d_predict)
        self.alg.fit(self.df[self.predictors], self.df['home'])
        predictions_home = self.alg.predict(df_predict[self.predictors])
        self.alg.fit(self.df[self.predictors], self.df['away'])
        predictions_away = self.alg.predict(df_predict[self.predictors])

        print predictions_home
        print predictions_away
        return_score = [predictions_home[0],predictions_away[0]]
        return return_score



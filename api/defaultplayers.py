import falcon
import json
import sys
import csv
sys.path.append("indexing/")

class defaultplayers(object):

    def __init__(self):
        self.main_11 = {}

    def on_get(self, req, resp):
        with open('indexing/utilities/main-11.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.main_11[row['team_name']] = row['players'].strip()
        defaultplayers = self.main_11
        # defaultplayers['team1_players']=self.main_11[home]
        # defaultplayers['team2_players'] = self.main_11[away]

        resp.status = falcon.HTTP_201
        msg = {
            'defaultplayers': defaultplayers
        }
        resp.body = json.dumps(msg)

    def on_post(self, req, resp):
        data = req.stream.read(req.content_length or 0)
        team_names = json.loads(data)
        home = team_names['team1_name']
        away = team_names['team2_name']
        print home
        print away
        with open('indexing/utilities/main-11.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.main_11[row['team_name']] = row['players'].strip()
        defaultplayers = {}
        defaultplayers['team1_players']=self.main_11[home]
        defaultplayers['team2_players'] = self.main_11[away]

        resp.status = falcon.HTTP_201
        msg = {
            'defaultplayers': defaultplayers
        }
        resp.body = json.dumps(msg)
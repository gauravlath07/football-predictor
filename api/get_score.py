import falcon
import json
from indexing.predict import predict
import sys
sys.path.append("indexing/")

class get_score(object):

    def __init__(self):
        self.predict_instance = predict()

    def on_get(self, req, resp):
        msg = {
            'score': '100!'
        }
        resp.body = json.dumps(msg)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = req.stream.read(req.content_length or 0)
        player_json = json.loads(data)
        # print type(player_json)
        result = self.predict_instance.process_new_feature(player_json)
        result = str(result)
        resp.status = falcon.HTTP_201
        msg = {
            'score': result
        }
        resp.body = json.dumps(msg)
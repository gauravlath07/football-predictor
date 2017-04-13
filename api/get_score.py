import falcon
import json

class get_score(object):

    def on_get(self, req, resp):
        msg = {
            'score': '100!'
        }
        resp.body = json.dumps(msg)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = req.stream.read(req.content_length or 0)
        print data
        resp.status = falcon.HTTP_201
        msg = {
            'score': '100'
        }
        resp.body = json.dumps(msg)
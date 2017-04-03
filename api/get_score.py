import falcon

class get_score(object):

    def on_get(self, req, resp):
        msg = {
            'score': '100!'
        }

        resp.body = json.dumps(msg)
        # This line can be ommited, because 200 is the default code falcon
        # returns, but it shows how you can set a status code.
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        print req.stream.read()
        resp.status = falcon.HTTP_201
         msg = {
            'score': '100!'
        }

        resp.body = json.dumps(msg)
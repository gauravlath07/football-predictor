import falcon
from get_score import get_score

api = application = falcon.API()

score = get_score()
api.add_route('/get_score', score)
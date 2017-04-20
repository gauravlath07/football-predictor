import falcon
from get_score import get_score
from defaultplayers import defaultplayers
from falcon_cors import CORS

cors = CORS(allow_origins_list=['http://localhost:3000'],allow_all_origins=True, allow_all_headers=True, allow_all_methods=True, allow_credentials_all_origins=True)
api = application =falcon.API(middleware=[cors.middleware])

score = get_score()
defaultplayers = defaultplayers()

api.add_route('/get_score', score)
api.add_route('/get_defaultplayers', defaultplayers)





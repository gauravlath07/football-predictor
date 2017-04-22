#!/usr/bin/env python
import falcon
import json

from falcon_cors import CORS

# end points
from get_score import get_score
from defaultplayers import defaultplayers

cors = CORS(allow_origins_list=['http://localhost:3000','http://football.gauravlath.xyz'],allow_all_origins=True, allow_all_headers=True, allow_all_methods=True, allow_credentials_all_origins=True)
api = falcon.API(middleware=[cors.middleware])

score = get_score()
defaultplayers = defaultplayers()

api.add_route('/get_score', score)
api.add_route('/get_defaultplayers', defaultplayers)







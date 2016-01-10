#!/usr/bin/env python3
import falcon
from lib import server_api


api = falcon.API()
api.add_route('/', server_api.GetStatus())
api.add_route('/api/ping', server_api.Ping())

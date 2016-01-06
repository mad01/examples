#!/usr/bin/env python
import falcon
from lib import server_api


api = falcon.API()
api.add_route('/api/create/account', server_api.CreateAcount())
api.add_route('/api/get/account', server_api.GetAcount())

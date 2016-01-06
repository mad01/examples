#!/usr/bin/env python
import json
import falcon
from . import py_proto_pb2 as proto


class Server(object):

    def __init__(self):
        self.proto = proto
        pass

    def login(self):
        pass

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'HTTPError', ex.message)

        try:
            json_data = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'JSON was incorrect.')

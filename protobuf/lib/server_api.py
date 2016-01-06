#!/usr/bin/env python
import json
import falcon
from . import py_proto_pb2 as proto


def validate_content_type(content):
    if content == 'application/x-protobuf':
        return True
    else:
        return False


def proto_error(errorCode='', message=''):
    command = proto.ErrorDTO()
    command.message = message
    command.errorCode = errorCode
    command.SerializeToString()
    return command


class CreateAcount(object):

    def __init__(self):
        self.proto = proto

    def on_post(self, req, resp):
        if not validate_content_type(req.content_type):
            error_data = proto_error(
                errorCode=3,
                message='incorrect content_type'
                )
            resp.status = falcon.HTTP_400
            resp.body = error_data

        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'HTTPError', ex.message)

        try:
            json_data = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'JSON was incorrect.')


class GetAcount(object):

    def __init__(self):
        self.proto = proto

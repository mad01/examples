#!/usr/bin/env python
import falcon
from . import py_proto_pb2 as proto


def validate_content_type(content):
    if content == 'application/x-protobuf':
        return True
    else:
        return False


def proto_http_type():
    return 'application/x-protobuf'


def proto_error(errorType='', message=''):
    command = proto.ErrorDTO()
    command.message = message
    command.errorCode = errorType
    command.SerializeToString()
    return command


class GetStatus(object):

    def on_get(self, req, resp):
        resp.body = '{"status": "hello"}'


class Ping(object):

    def __init__(self):
        self.proto = proto

    def on_post(self, req, resp):
        if not validate_content_type(req.content_type):
            errorMessage = 'content_type is: %s' % (req.content_type)
            data = proto_error(
                errorCode=proto.INCORRECT_CONTENT_TYPE,
                message=errorMessage
                )
            resp.content_type = proto_http_type()
            resp.status = falcon.HTTP_400
            resp.data = data

        try:
            command = proto.PingCommand()
            command.ParseFromString(req.stream.read())
            assert command.ping.HasField('msg')
            assert command.ping.HasField('channel')
            assert command.ping.HasField('pingId')

            print(command.ping.msg)
            print(command.ping.channel)
            print(command.ping.pingId)

            cmd = proto.PingDocument()
            ping = cmd.ping
            ping.msg = command.ping.msg
            ping.channel = command.ping.channel
            ping.pingId = proto.PONG

            resp.content_type = proto_http_type()
            resp.status = falcon.HTTP_201
            resp.data = cmd.SerializeToString()

        except AssertionError as e:
            errorMessage = 'AssertionError: %s' % (e.message)
            data = proto_error(
                errorCode=proto.INVALID_REQUEST,
                message=errorMessage
                )
            resp.content_type = proto_http_type()
            resp.status = falcon.HTTP_400
            resp.data = data

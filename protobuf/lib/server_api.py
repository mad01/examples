#!/usr/bin/env python
import falcon
from . import py_proto_pb2 as proto


def validate_content_type(content):
    if content == 'application/x-protobuf':
        return True
    else:
        return False


def proto_error(errorType='', message=''):
    command = proto.ErrorDTO()
    command.message = message
    command.errorCode = errorType
    command.SerializeToString()
    return command


class CreateAcount(object):

    def __init__(self):
        self.proto = proto

    def on_post(self, req, resp):
        if not validate_content_type(req.content_type):
            errorMessage = 'content_type is: %s' % (req.content_type)
            data = proto_error(
                errorCode=proto.INCORRECT_CONTENT_TYPE,
                message=errorMessage
                )
            resp.status = falcon.HTTP_400
            resp.body = data

        try:
            command = proto.CreateAccountCommand()
            command.ParseFromString(req.stream.read())
            assert command.HasField('accountUid')
            assert command.HasField('accountName')
            assert command.HasField('accountType')
            assert command.HasField('password')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'HTTPError', ex.message)


class GetAcount(object):

    def __init__(self):
        self.proto = proto

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
            assert command.account.HasField('accountUid')
            assert command.account.HasField('accountName')
            assert command.account.HasField('password')

            cmd = proto.CreateAccountDocument()
            cmd.account = command
            cmd.SerializeToString()
            resp.status = falcon.HTTP_201
            resp.body = cmd
        except AssertionError as e:
            errorMessage = 'AssertionError: %s' % (e.message)
            data = proto_error(
                errorCode=proto.INVALID_REQUEST,
                message=errorMessage
                )
            resp.status = falcon.HTTP_400
            resp.body = data


class GetAcount(object):

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
            command = proto.GetAccountCommand()
            command.ParseFromString(req.stream.read())
            assert command.HasField('accountName')

            cmd = proto.GetAccountDocument()
            cmd.account = ''  # fix some get accountDTO thing
            cmd.SerializeToString()
            resp.status = falcon.HTTP_201
            resp.body = cmd
        except AssertionError as e:
            errorMessage = 'AssertionError: %s' % (e.message)
            data = proto_error(
                errorCode=proto.INVALID_REQUEST,
                message=errorMessage
                )
            resp.status = falcon.HTTP_400
            resp.body = data

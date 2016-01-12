#!/usr/bin/env python3
from . import py_proto_pb2 as proto


class ProtoShared(object):

    def __init__(self):
        pass

    def proto_error_handler(self, resp):
        command = proto.ErrorDTO()
        command.ParseFromString(resp)
        return command

    def proto_error_name(self, number):
        return proto.ErrorCodeDTO.Name(number)

    def proto_error_value(self, val):
        return proto.ErrorCodeDTO.Value(val)

    def pingValue(self, ping):
        return proto.PingIdDTO.Value(ping)

    def pingName(self, ping):
        return proto.PingIdDTO.Name(ping)

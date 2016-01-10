#!/usr/bin/env python
import requests
from . import py_proto_pb2 as proto


class Client(object):

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/x-protobuf",
            "Accept": "application/x-protobuf"
        })

    def proto_error_handler(self, resp):
        command = proto.ErrorDTO()
        command.ParseFromString(resp)
        return command

    def proto_error_name(self, number):
        return proto.ErrorCodeDTO.Name(number)

    def pingId(self, ping):
        return proto.PingIdDTO.Value(ping)

    def build_url(self, urn):
        url = 'http://%s:8000/%s' % ('127.0.0.1', urn)
        return url

    def send_ping(self, msg='', channel='', pingId=''):
        url = self.build_url('api/ping')
        command = proto.PingCommand()
        ping = command.ping
        ping.msg = str(msg)
        ping.channel = str(channel)
        ping.pingId = self.pingId(pingId)

        res = self.session.post(url, data=command.SerializeToString())
        if (res.status_code == 201):
            cmd = proto.PingDocument()
            cmd.ParseFromString(res.content)
            return cmd
        else:
            print(res.text)
            return self.proto_error_handler(res.content)

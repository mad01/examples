#!/usr/bin/env python3
import requests
from . import py_proto_pb2 as proto
from .shared import ProtoShared


class Client(object):

    def __init__(self):
        self.shared = ProtoShared()
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/x-protobuf",
            "Accept": "application/x-protobuf"
        })

    def build_url(self, urn):
        url = 'http://%s:8000/%s' % ('127.0.0.1', urn)
        return url

    def send_ping(self, msg='', channel='', pingId=''):
        url = self.build_url('api/ping')
        command = proto.PingCommand()
        command.ping.msg = str(msg)
        command.ping.channel = str(channel)
        command.ping.pingId = self.shared.pingValue(pingId)

        res = self.session.post(url, data=command.SerializeToString())
        if (res.status_code == 201):
            cmd = proto.PingDocument()
            cmd.ParseFromString(res.content)
            return cmd
        else:
            print(res.text)
            return self.proto_error_handler(res.content)

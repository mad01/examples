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

    def build_url(self, urn):
        url = 'http://%s/%s' % ('127.0.0.1', urn)
        return url

    def create_account(self, accountUid='', email='', password=''):
        url = self.build_url('api/create/account')
        command = proto.CreateAccountCommand()
        command.account.accountUid = accountUid
        command.account.accountName = email
        command.account.password = password

        res = self.session.post(url, data=command.SerializeToString())
        if (res.status_code != 200):
            print(res.text)
            return self.proto_error_handler(res.content)
        else:
            cmd = proto.CreateAccountDocument()
            cmd.ParseFromString(res.content)
            return cmd

    def get_account(self, email=''):
        url = self.build_url('api/get/account')
        command = proto.GetAccountCommand()
        command.accountName = email

        res = self.session.post(url, data=command.SerializeToString())
        if (res.status_code != 200):
            print(res.text)
            return self.proto_error_handler(res.content)
        else:
            cmd = proto.GetAccountDocument()
            cmd.ParseFromString(res.content)
            return cmd

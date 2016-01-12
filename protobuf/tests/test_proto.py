#!/usr/bin/env python
import unittest
from lib import client_api
from lib.shared import ProtoShared


class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.shared = ProtoShared()
        self.api = client_api.Client()

    def test_ping(self):
        msg = 'hello'
        channel = 'foo'
        cmd = self.api.send_ping(
            msg=msg,
            channel=channel,
            pingId='PING'
            )
        self.assertEqual(cmd.ping.pingId, self.shared.pingValue('PONG'))
        self.assertEqual(cmd.ping.msg, msg)
        self.assertEqual(cmd.ping.channel, channel)

if __name__ == '__main__':
    unittest.main()

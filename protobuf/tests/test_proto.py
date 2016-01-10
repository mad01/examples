#!/usr/bin/env python
import unittest
from lib import server_api
from lib import client_api


class TestServer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = server_api.Server()
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = client_api.Client()
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ping(self):
        msg = 'hello'
        channel = 'foo'
        cmd = self.api.send_ping(
            msg=msg,
            channel=channel,
            pingId='PING'
            )
        self.assertEqual(cmd.ping.pingId, self.api.pingId('PONG'))
        self.assertEqual(cmd.ping.msg, msg)
        self.assertEqual(cmd.ping.channel, channel)

if __name__ == '__main__':
    unittest.main()

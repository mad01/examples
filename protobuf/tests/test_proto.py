#!/usr/bin/env python
import unittest
from lib import server_api
from lib import client_api
from lib import util


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

    def test_create_account(self):
        accountUid = util.random_hex()
        email = util.random_email(domain='example.com')
        res = self.api.create_account(
            accountUid=accountUid,
            email=email,
            password='Qwerty123'
            )
        self.assertEqual(res.status_code, 200)

    def test_get_account(self):
        pass

if __name__ == '__main__':
    unittest.main()

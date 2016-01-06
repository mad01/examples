#!/usr/bin/env python
import unittest
from lib import api


class TestServer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = api.Server()
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example_exept_broken(self):
        self.assertTrue(False)

    def test_example_exept_working(self):
        self.assertFalse(False)


class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = api.Client()
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example_exept_broken(self):
        self.assertTrue(False)

    def test_example_exept_working(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()

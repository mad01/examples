#!/usr/bin/env python2
import unittest


class TestEx(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.username = 'foobar123@example.com'
        self.password = 'Qwerty123@'

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertTrue(True)

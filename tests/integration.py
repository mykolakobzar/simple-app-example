# -*- coding: utf-8 -*-
"""
    :author: Nicholas Kobzar
    :repo: https://github.com/n-g-s/simple-app.git
"""

from app import app
import unittest


class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        request = self.app.get('/')
        assert request.status == '200 OK'

    def test_liveness(self):
        request = self.app.get('/status/alive')
        assert request.status == '200 OK'

    def test_readiness(self):
        request = self.app.get('/status/ready')
        assert b'ready' in request.data

    def test_404(self):
        request = self.app.get('/something_new')
        self.assertEqual(request.status, '404 NOT FOUND')

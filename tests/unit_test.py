# -*- coding: utf-8 -*-
"""
    :author: Nicholas Kobzar
    :repo: https://github.com/n-g-s/simple-app.git
"""

import unittest
from timer import timer


class TimerTest(unittest.TestCase):

    def test_timer_instance(self):
        self.assertIsInstance(timer.app_readiness(), tuple)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import task4
import unittest


class TaskTest(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_dojob(self):
        self.assertEqual(task4.dojob(13), -1)
        self.assertEqual(task4.dojob(10), 25)
        self.assertEqual(task4.dojob(144), 289)
        self.assertEqual(task4.dojob(5), 15)

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()

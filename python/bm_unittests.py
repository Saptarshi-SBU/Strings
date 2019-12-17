#!/usr/bin/python

import unittest
from bm import BoyerMooreSearch

class BMTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        text    = 'abrabrakadabra'
        pattern = 'raka'
        self.assertEqual(BoyerMooreSearch(text.lower(), pattern.lower()), True, \
            "match failure")

    def test_case_002(self):
        text    = 'xpbctbxabpqxctbpq'
        pattern = 'tpabccxab'
        self.assertEqual(BoyerMooreSearch(text.lower(), pattern.lower()), False, \
            "bad match")

    def test_case_003(self):
        text    = 'xpbctbxabpqxctbpq'
        pattern = 'txabccxab'
        self.assertEqual(BoyerMooreSearch(text.lower(), pattern.lower()), False, \
            "bad match")

    def test_case_004(self):
        text    = 'xpbctbxqbcpqxpqbpq'
        pattern = 'pqbpq'
        self.assertEqual(BoyerMooreSearch(text.lower(), pattern.lower()), True, \
            "match failure")

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(BMTestCase('test_case_001'))
    suite.addTest(BMTestCase('test_case_002'))
    suite.addTest(BMTestCase('test_case_003'))
    suite.addTest(BMTestCase('test_case_004'))
    runner.run(suite)

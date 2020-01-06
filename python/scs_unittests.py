#!/usr/bin/python

import unittest
from scs import scs
from utils_collections import permutation, overlapped_string

class scsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        nr = 6
        ans = []
        permutation(nr, ans)
        for i in range(len(ans)):
            print '{}.{}'.format(i + 1, ans[i])
        self.assertEqual(len(ans), 720, "incorrect result")

    def test_case_002(self):
        ans = overlapped_string('red', 'red')
        print ans
        self.assertEqual(len(ans), 3, "incorrect result")

    def test_case_003(self):
        wlist = [ 'red1', 'red', 'bad']
        ans = scs(wlist)
        print ans
        self.assertEqual(len(ans), 7, "incorrect result")

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(scsTestCase('test_case_001'))
    suite.addTest(scsTestCase('test_case_002'))
    suite.addTest(scsTestCase('test_case_003'))
    runner.run(suite)

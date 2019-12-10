#!/usr/bin/python

import unittest
from lcs import LCS

class LCSTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        textp = "algoritghgr"
        textq = "grithm"

        l1, texta = LCS(textp, textq).sequence()
        print 'lcs {}'.format(l1)
        print 'textp: {}'.format(textp)
        print 'texta: {}'.format(texta)
        l2, texta = LCS(textp, textq).sequenceDP()
        print 'lcs {}'.format(l2)
        print 'textp: {}'.format(textp)

        print ('text {} pattern {} lcs {}/{}'.format(textp, textq, l1, l2))
        self.assertEqual(l1, l2, "lcs length mismatch")

    def test_case_002(self):
        textp = "algoritghgr"
        textq = "agrithm"

        l1, texta = LCS(textp, textq).sequence()
        print 'lcs {}'.format(l1)
        print 'textp: {}'.format(textp)
        print 'texta: {}'.format(texta)
        l2, texta = LCS(textp, textq).sequenceDP()
        print 'lcs {}'.format(l2)
        print 'textp: {}'.format(textp)

        print ('text {} pattern {} lcs {}/{}'.format(textp, textq, l1, l2))
        self.assertEqual(l1, l2, "lcs length mismatch")

    def test_case_003(self):
        textp = "aaaaaabbb"
        textq = "ab"

        l1, texta = LCS(textp, textq).sequence()
        print 'lcs {}'.format(l1)
        print 'textp: {}'.format(textp)
        print 'texta: {}'.format(texta)
        l2, texta = LCS(textp, textq).sequenceDP()
        print 'lcs {}'.format(l2)
        print 'textp: {}'.format(textp)

        print ('text {} pattern {} lcs {}/{}'.format(textp, textq, l1, l2))
        self.assertEqual(l1, l2, "lcs length mismatch")

    def test_case_004(self):
        textp = "aaaaaabbbcd"
        textq = "abc"

        l1, texta = LCS(textp, textq).sequence()
        print 'lcs {}'.format(l1)
        print 'textp: {}'.format(textp)
        print 'texta: {}'.format(texta)
        l2, texta = LCS(textp, textq).sequenceDP()
        print 'lcs {}'.format(l2)
        print 'textp: {}'.format(textp)

        print ('text {} pattern {} lcs {}/{}'.format(textp, textq, l1, l2))
        self.assertEqual(l1, l2, "lcs length mismatch")

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(LCSTestCase('test_case_001'))
    suite.addTest(LCSTestCase('test_case_002'))
    suite.addTest(LCSTestCase('test_case_003'))
    suite.addTest(LCSTestCase('test_case_004'))
    runner.run(suite)

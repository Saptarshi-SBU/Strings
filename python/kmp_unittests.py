#!/usr/bin/python

import unittest
from kmp import ComputePrefixTable, KMPMatch

class KMPTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        text = "ABBCABCDABA"
        pattern = "ABBCABCDABA"
        self.assertEqual(KMPMatch(text, pattern, ComputePrefixTable(pattern)), \
            1, "incorrect count")

    def test_case_002(self):
        text = "AB"
        pattern = "ABBCABCDABA"
        self.assertEqual(KMPMatch(text, pattern, ComputePrefixTable(pattern)), \
            0, "incorrect count")

    def test_case_003(self):
        text = "ABBCABCDABA"
        pattern = "AB"
        self.assertEqual(KMPMatch(text, pattern, ComputePrefixTable(pattern)), \
            3, "incorrect count")

    def test_case_004(self):
        text = "ABBCABCDABA"
        pattern = "ABC"
        self.assertEqual(KMPMatch(text, pattern, ComputePrefixTable(pattern)), \
            1, "incorrect count")

    def test_case_005(self):
        text = "ABCAABCEABCD"
        pattern = "ABCD"
        self.assertEqual(KMPMatch(text, pattern, ComputePrefixTable(pattern)), \
            1, "incorrect count")

    def test_case_006(self):
        text = "ABCAABCDEABCD"
        pattern = "ABCD"
        self.assertEqual(KMPMatch(text, pattern, ComputePrefixTable(pattern)), \
            2, "incorrect count")

    def test_case_007(self):
        text = "ABCDABDABCDABCAB"
        pattern = "ABCDABC"
        self.assertEqual(KMPMatch(text, pattern, ComputePrefixTable(pattern)), \
            1, "incorrect count")

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(KMPTestCase('test_case_001'))
    suite.addTest(KMPTestCase('test_case_002'))
    suite.addTest(KMPTestCase('test_case_003'))
    suite.addTest(KMPTestCase('test_case_004'))
    suite.addTest(KMPTestCase('test_case_005'))
    suite.addTest(KMPTestCase('test_case_006'))
    suite.addTest(KMPTestCase('test_case_007'))
    runner.run(suite)

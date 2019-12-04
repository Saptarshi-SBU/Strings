#!/usr/bin/python

import unittest
from suffix_array import BuildSuffixArrayWithPrefixDouble, \
    BuildSuffixArrayNaive, CountOccurences
from lcp import LCP

class SuffixArrayTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        text = "ACTAGAGACTTTAGACT"
        pattern = "ACT"
        suffix_array_naive = BuildSuffixArrayNaive(text)
        print suffix_array_naive
        sa = [ text[x : len(text)] for x in suffix_array_naive]
        #sa = sa.pop()
        sa = sa[1 : len(sa)]
        print (sa)
        print sorted([ text[i : len(text)] for i in range(len(text)) ])
        self.assertEqual(sa,
            (sorted([ text[i : len(text)] for i in range(len(text)) ])), " suffix array mismatch")
        occ = CountOccurences(text, pattern, suffix_array_naive)
        print ('text {} pattern {} occ {}'.format(text, pattern, occ))
        self.assertEqual(occ, 3, "pattern occurences mismatch")

    def test_case_002(self):
        text = "ACTAGAGACTTTAGACT"
        pattern = "ACT"
        suffix_array_pd = BuildSuffixArrayWithPrefixDouble(text)
        sa = [ text[x : len(text)] for x in suffix_array_pd]
        #sa = sa.pop()
        sa = sa[1 : len(sa)]
        print (sa)
        self.assertEqual(sa,
            (sorted([ text[i : len(text)] for i in range(len(text)) ])), "suffix array mismatch")
        occ = CountOccurences(text, pattern, suffix_array_pd)
        print ('text {} pattern {} occ {}'.format(text, pattern, occ))
        self.assertEqual(occ, 3, "pattern occurences mismatch")

    def test_case_003(self):
        text = "ACTAGAGACTTTAGACT"
        suffix_array_pd = BuildSuffixArrayWithPrefixDouble(text)
        lcp = LCP(text, suffix_array_pd)
        print (lcp)

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(SuffixArrayTestCase('test_case_001'))
    suite.addTest(SuffixArrayTestCase('test_case_002'))
    suite.addTest(SuffixArrayTestCase('test_case_003'))
    runner.run(suite)

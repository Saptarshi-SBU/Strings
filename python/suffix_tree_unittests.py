#!/usr/bin/python

import unittest
from lcp import LCP
from suffix_array import BuildSuffixArrayWithPrefixDouble
from suffix_tree import SuffixTree

class SuffixTreeTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        text = "ACAACTTACT"
        suffix_array = BuildSuffixArrayWithPrefixDouble(text)
        #print suffix_array
        lcp = LCP(text, suffix_array)
        #print lcp
        text = text + '$'
        suffix_array.pop(0)
        suffix_tree = SuffixTree()
        suffix_tree.buildFromSuffixArray(text, suffix_array, lcp)
        suffix_tree.printSuffixTree(text)

    def test_case_002(self):
        text = "ACTAGAGACTTTAGACT"
        suffix_array = BuildSuffixArrayWithPrefixDouble(text)
        #print suffix_array
        lcp = LCP(text, suffix_array)
        #print lcp
        text = text + '$'
        suffix_array.pop(0)
        suffix_tree = SuffixTree()
        suffix_tree.buildFromSuffixArray(text, suffix_array, lcp)
        suffix_tree.printSuffixTree(text)

    def test_case_003(self):
        text = "ACAGACTTTAGACT"
        suffix_array = BuildSuffixArrayWithPrefixDouble(text)
        #print suffix_array
        lcp = LCP(text, suffix_array)
        #print lcp
        text = text + '$'
        suffix_array.pop(0)
        suffix_tree = SuffixTree()
        suffix_tree.buildFromSuffixArray(text, suffix_array, lcp)
        suffix_tree.printSuffixTree(text)

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(SuffixTreeTestCase('test_case_001'))
    runner.run(suite)

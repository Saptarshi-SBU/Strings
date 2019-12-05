#!/usr/bin/python

import unittest
from lcp import LCP
from suffix_array import BuildSuffixArrayWithPrefixDouble
from suffix_tree import SuffixTree

#need biopython for processing real-life sequences
import Bio
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
#Refs: http://biopython.org/DIST/docs/tutorial/Tutorial.html#chapter:entrez

class SuffixTreeTestCase(unittest.TestCase):
    def setUp(self):
        pass

    #@unittest.skip('Skipping test')
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

    #@unittest.skip('Skipping test')
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

    #@unittest.skip('Skipping test')
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

    #@unittest.skip('Skipping test')
    def test_case_004(self):
        Entrez.email = "A.N.Other@example.com"
        #gb : genebank
        handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")
        print (record)
        text = str(record.seq)
        handle.close()
        #text = text[0 : 32]
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
    suite.addTest(SuffixTreeTestCase('test_case_002'))
    suite.addTest(SuffixTreeTestCase('test_case_003'))
    suite.addTest(SuffixTreeTestCase('test_case_004'))
    runner.run(suite)

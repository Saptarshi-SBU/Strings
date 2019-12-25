#!/usr/bin/python

import unittest
from bktree import CreateBkTree, ApproximateMatch

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class BKTreeTestCase(unittest.TestCase):
    def setUp(self):
        text= """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard"""
        tokenized_text = word_tokenize(text)
        self.bktree = CreateBkTree(tokenized_text)

    def test_case_001(self):
        pattern = "bat"
        approx_match_list = ApproximateMatch(self.bktree, pattern, 1)
        expect_match_list =  [ "eat" ]
        print 'pattern: {} - {}'.format(pattern, approx_match_list)
        self.assertEqual(approx_match_list, expect_match_list)  

    def test_case_002(self):
        pattern = "ski"
        approx_match_list = ApproximateMatch(self.bktree, pattern, 1)
        expect_match_list =  [ "sky" ]
        print 'pattern: {} - {}'.format(pattern, approx_match_list)
        self.assertEqual(approx_match_list, expect_match_list)  

    def test_case_003(self):
        pattern = "awsome"
        approx_match_list = ApproximateMatch(self.bktree, pattern, 1)
        expect_match_list =  [ "awesome" ]
        print 'pattern: {} - {}'.format(pattern, approx_match_list)

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    nltk.download('punkt')
    suite.addTest(BKTreeTestCase('test_case_001'))
    suite.addTest(BKTreeTestCase('test_case_002'))
    suite.addTest(BKTreeTestCase('test_case_003'))
    runner.run(suite)

#!/usr/bin/python

import unittest
from suffix_trie import SuffixTrie

class SuffixTrieTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        doc = []
        s1 = "Las Vegas$"
        s2 = "Trip to Las Vegas$"
        s3 = "Sanata Clara$"
        doc.append(s1)
        doc.append(s2)
        doc.append(s3)
        suffix_trie = SuffixTrie()
        for i in reversed(range(len(s1))):
            suffix_trie.add(s1[i:], doc.index(s1))
        for i in reversed(range(len(s2))):
            suffix_trie.add(s2[i:], doc.index(s2))
        for i in reversed(range(len(s3))):
            suffix_trie.add(s3[i:], doc.index(s3))
        suffix_trie.show(suffix_trie.root)
        self.assertEqual(suffix_trie.match("Las"), [0, 1], 'incorrect match')

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(SuffixTrieTestCase('test_case_001'))
    suite.addTest(SuffixTrieTestCase('test_case_002'))
    runner.run(suite)

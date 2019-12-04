#!/usr/bin/python

import unittest

def ComputePrefixTable(pattern):
    ''' Prefix Function for pattern preprocess (concept : border strings) '''

    prefixTable = [0 for x in pattern ]
    for i in range(len(pattern)):
        if i == 0:
            prefixTable[i] = 0
        else:
            if pattern[prefixTable[i - 1]] == pattern[i]:
                prefixTable[i] = 1 + prefixTable[i - 1]
            else:
                for k in reversed(range(i)):
                    if k != 0 and pattern[prefixTable[k]] != pattern[i]:
                        continue
                    prefixTable[i] = prefixTable[k]
                    break
    return prefixTable                

def KMPMatch(string, pattern, prefixTable):
    ''' KMP algorithm '''

    i = p = c = 0
    N = len(string)
    P = len(pattern)

    #print string
    #print pattern
    #print prefixTable

    while i < N:
        print '==>{}:{} {}:{}'.format(i, string[i], p, pattern[p])
        if string[i] == pattern[p]:
            p = p + 1
            i = i + 1
        # pattern mismatch, shift pattern by next possible prefix
        elif p > 0:
            p = max(prefixTable[p - 1] - 1, 0)
        # move to next segment in text    
        else:
            i = i + 1
            #print ('{}/{}'.format(string[i : i + N],
            #    pattern[p : p + P]))

        # Match
        if p == len(pattern):
            c = c + 1
            i = i - (p - 1) + 1
            p = 0
        #print '<=={}:{}'.format(i, p)
    return c

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

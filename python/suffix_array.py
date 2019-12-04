#!/usr/bin/python

import sys
import math

class PrefixRank(object):
    
    def __init__(self):
        ''' ctor '''
                # start index of the suffix in original string
        self.originalIndex = -1
                # rank of old portion of suffix string
        self.firstHalf  = -1
                # rank of new portion of suffix string
        self.secondHalf = -1
        # current length
        self.length = 0

    def compare(self, rhObj):
        ''' multi-key attribute comparator '''

        res = self.firstHalf - rhObj.firstHalf
        if res:
            return res
        else:
            return self.secondHalf - rhObj.secondHalf

    def debugstring(self, string):
        ''' debug string '''

        start = self.originalIndex
        end   = start + self.length
        return ('index:{}/{}\t suffix:{}\t rank:{}-{}'.format(start, end, string[start : end], \
            self.firstHalf, self.secondHalf))

def PrefixRankCompare(r1, r2):
    ''' Compare ranks '''

    return r1.compare(r2)

def LexicalRankCompare(r1, r2):
    ''' Compare ranks '''

    if r1.firstHalf == r2.firstHalf:
        return 0
    elif r1.firstHalf < r2.firstHalf:
        return -1
    else:
        return 1

def BuildSuffixArrayWithPrefixDouble(string):
    ''' Builds suffix array using Prefix Doubling '''

    string = string + '$'
    N = len(string)

    # generator
    suffixObjects = [ PrefixRank() for i in range(N) ]

    # construct and initialize rank map
    rankMap = [ [ 0 for i in range(N) ] for i in range(int(math.log(N, 2)) + 1) ] 
    for i in range(N):
        rankMap[0][i] = ord(string[i]) - ord('$')
        print ('prefix : {} rank :{}'.format(string[i], rankMap[0][i]))

    # prefix doubling algorithm for sorting suffixes
    for k in range(0, int(math.log(N, 2)) + 1): # range excludes the end
        # update prefix length 
        length = int(pow(2, k))
        print ('prefix length : k={}/length={}/N={}'.format(k, length, N)) 

        # update suffix entries ranking
        for i in range(N):
            suffixObjects[i].originalIndex = i
            suffixObjects[i].firstHalf  = rankMap[k][i]
            if i + length/2 < N: 
                suffixObjects[i].secondHalf = rankMap[k][i + length/2] 
            else:
                suffixObjects[i].secondHalf = 0
            suffixObjects[i].length = min(length, N)
 
        # sort suffixes entries with updated ranking
        suffixObjects.sort(PrefixRankCompare)

        # print suffices
        for i in suffixObjects:
            print i.debugstring(string);

        # update rank map with new prefix length
        for i in range(N):
            if k + 1 > math.log(N, 2):
                break
            if i == 0 or suffixObjects[i].compare(suffixObjects[i - 1]) != 0:
                rankMap[k + 1][suffixObjects[i].originalIndex] = i
            else:
                rankMap[k + 1][suffixObjects[i].originalIndex] = \
                    rankMap[k + 1][suffixObjects[i - 1].originalIndex]
    # final array
    return [ x.originalIndex for x in suffixObjects ]   

def BuildSuffixArrayNaive(string):
    ''' Builds suffix array'''

    string = string + '$'
    N = len(string)

    suffixObjects = [ PrefixRank() for i in range(N) ]
    for i in range(N):
        suffixObjects[i].originalIndex = i
        suffixObjects[i].length = N - i
        suffixObjects[i].firstHalf = string[i : N]

    suffixObjects.sort(LexicalRankCompare)
    for i in suffixObjects:
        print i.debugstring(string);

    # final array
    return [ x.originalIndex for x in suffixObjects ]   

def CountOccurences(string, pattern, sf):
    ''' Count Occurences '''

    topIndex = midIndex = 0
    N = bottomIndex = len(string)
    P = len(pattern)
    midIndex = N

    # lower bound
    while topIndex < bottomIndex:
        midIndex = (topIndex + bottomIndex) / 2
        suffix = string[sf[midIndex] : sf[midIndex] + P]
        print ('==>lb top{} mid{} bottom{} {}'.format(topIndex, midIndex, bottomIndex, suffix))
        if suffix < pattern:
            topIndex = midIndex + 1
        else:
            bottomIndex = midIndex
        print ('<==lb top{} mid{} bottom{} {}'.format(topIndex, midIndex, bottomIndex, suffix))

    start = midIndex
    bottomIndex = midIndex = N

    # upper bound
    while topIndex < midIndex:
        midIndex = (topIndex + bottomIndex) / 2
        suffix = string[sf[midIndex] : sf[midIndex] + P]
        print ('==>ub top{} mid{} bottom{} {}'.format(topIndex, midIndex, bottomIndex, suffix))
        assert pattern <= suffix
        if pattern == suffix:
            topIndex = midIndex + 1
        else:
            bottomIndex = midIndex;
        print ('<==ub top{} mid{} bottom{} {}'.format(topIndex, midIndex, bottomIndex, suffix))

    return midIndex - start

#http://web.cs.iastate.edu/~cs548/references/linear_lcp.pdf
def LCP(string, suffix_array):
    ''' Longest Commmon Prefix Array Computation (LCP) '''
    h = 0
    Height = {}
    inv_suffix_array = {}

    N = len(suffix_array)
    #print (suffix_array)
    string = string + '$'
    assert len(string) == N

    # compute inverse suffix-array
    for i in range(N):
        #print (i)
        #print (suffix_array[i])
        inv_suffix_array[suffix_array[i]] = i
    # compute lcp
    # scan in original string order, find corresponding pair rank-wise
    # For next pair, common prefix will decrement by 1
    for i in range(N):
        if inv_suffix_array[i] > 0:
            k = suffix_array[inv_suffix_array[i] - 1]
            while (k + h) < N and (i + h) < N and string[k + h] == string[i + h]:
                h = h + 1
            Height[inv_suffix_array[i]] = h
            if h > 0:
                h = h - 1
    # lcp
    print ('LCP {}'.format(Height))
    return Height

if __name__ == "__main__":
    #string = sys.stdin.readline.strip()
    #string = "ACTAGAGACTTTAG"
    string = "ACTAGAGACTTTAGACT"
    suffix_array = BuildSuffixArrayWithPrefixDouble(string)
    print (suffix_array)
    suffix_array = BuildSuffixArrayNaive(string)
    print (suffix_array)
    print (sorted([ string[i : len(string)] for i in range(len(string)) ]))
    LCP(string, suffix_array)
    pattern = "ACT"
    occ = CountOccurences(string, pattern, suffix_array)
    print ('string {} pattern {} occ {}'.format(string, pattern, occ))

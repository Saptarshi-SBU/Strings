#!/usr/bin/python

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
        #print '==>{}:{} {}:{}'.format(i, string[i], p, pattern[p])
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

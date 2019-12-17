#!/usr/bin/python
#
# refs : https://web.cs.ucdavis.edu/~gusfield/cs224f11/bnotes.pdf

from string import ascii_lowercase

def RightMostOccurenceTable(pattern, alphabet):
    '''
        Bad character rule
    '''
    R = [ [] for i in pattern ]

    for i in range(len(pattern)):
        R[i] = {}
        for j in alphabet:
            R[i][j] = -1
            if j in pattern:
                # note : scan is from left to right, so rightmost    
                for k in range(len(pattern)):
                    if pattern[k] == j and k < i:
                        R[i][j] = k
    return R

def RightMostSuffixTable(pattern):
    '''
        Good-Suffix rule (weak)
    '''
    L = {}
    M = len(pattern)
    c = 0
    i = M - 1
    j = i - 1
    
    while j >= 0:
        if pattern[i] != pattern[j]:
            #print i, j
            j = j + c - 1
            i = M - 1
            c = 0
        else:
            #print pattern[i], pattern[j]
            if i not in L:
                L[i] = j
            c = c + 1
            i = i - 1
            j = j - 1
    print L
    for i in L:
        print pattern[i:], L[i]
    return L    

def BoyerMooreSearch(text, pattern):
    N = len(text)
    M = len(pattern)

    if M > N:
        print ('pattern greater in length')
        return False

    i = 0 #running index for text
    ns = 0 #shift count

    #for bad character rule
    R = RightMostOccurenceTable(pattern, ascii_lowercase)

    #for good character rule
    L = RightMostSuffixTable(pattern)
    while i < N:
        match = True
        for j in reversed(range(M)):
            #print 'i {} j {}'.format(i, j)
            if i + j >= N:
                print ('pattern shift exceeds text boundary, MISMATCH')
                return False
            elif pattern[j] != text[i + j]:
                match = False
                ch = text[i + j]
                # bad character rule
                if R[j][ch] < 0:
                    s1 = 1
                else:
                    s1 = j - R[j][ch]
                # good character rule
                if j + 1 in L:
                    s2 = j + 1 - L[j + 1]
                else:
                    s2 = 0
                print ('text suffix:{}-{} patt suffix: {}, shifts s1={}, s2={}'.format\
                    (i, text[i + j:], pattern[j:], s1, s2))
                i = i + max(s1, s2)
                ns = ns + 1
                break
            else:  
                pass

        if match:
            print ('pattern MATCH pos:{} {}/{}, shifts {}/{}'.format(i, text, pattern, ns, i))
            return True

    print ('pattern MISMATCH')
    return False

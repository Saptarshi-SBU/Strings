#!/usr/bin/python

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

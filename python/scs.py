#!/usr/bin/python
#
# Shortest SuperString Problem (Brute Force)
#
#

from utils_collections import permutation, overlapped_string

def scs(wlist):
    ''' shortest super string '''
    p = []
    ss = []
    nr = len(wlist)
    permutation(nr, p)
    for l in p:
        s = None
        for i in range(len(l)):
            if s is None:
                s = wlist[l[i]]
            else: 
                s = overlapped_string(s, wlist[l[i]])
        ss.append(s)
    return min(ss)   

wlist = [ 'red1', 'red', 'bad']
scs(wlist)

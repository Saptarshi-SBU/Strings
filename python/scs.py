#!/usr/bin/python
#
# Shortest SuperString Problem (Brute Force)
#
#
from utils_collections import permutation, overlapped_string

def scs(wlist):
    ''' shortest super string '''
    p = []
    ov = []
    nr = len(wlist)
    permutation(nr, p)
    for l in p:
        s = None
        for i in range(len(l)):
            if s is None:
                s = wlist[l[i]]
            else: 
                s = overlapped_string(s, wlist[l[i]])
        ov.append(s)
    return min(ov)   

wlist = [ 'red1', 'red', 'bad']
print scs(wlist)

def scs_greedy(wlist):
    ''' greedy super string based on overlap graph'''
    nr = len(wlist)
    overlap_graph = {}

    while True:
        ov = 0
        oi_max = oj_max = -1
        # create overlap graph with new nodes and edges based on overlapp distance
        for i in range(nr):
            for j in range(nr):
                if i == j:
                    continue
                op = wlist[i]
                oq = wlist[j]
                os = overlapped_string(op, oq)
                ol = overlap_graph[(op, oq)] = len(op) + len(oq) - len(os)
                if ol > ov:
                    ov = ol
                    ov_max = os
                    oi_max, oj_max = op, oq

        # update overlapped graph with the new combined node
        if oi_max >= 0:
            rkeys = [ k for k in overlap_graph.keys() if oi_max in k or oj_max in k ]
            for key in rkeys:
                del overlap_graph[key]

            wlist.pop(wlist.index(oi_max))
            wlist.pop(wlist.index(oj_max))
            wlist.append(ov_max)
            nr = len(wlist)
        else:
            break
    
    #concatenate disjoint nodes in the overlap graph
    return ''.join(wlist)

wlist = [ 'red1', 'red', 'bad']
print scs_greedy(wlist)

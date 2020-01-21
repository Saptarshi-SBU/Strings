#!/usr/bin/python
#
# Shortest SuperString Problem (Brute Force)
#
#
from utils_collections import permutation, overlapped_string

def ssp(wlist):
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
print ssp(wlist)

def ssp_greedy(wlist):
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
print ssp_greedy(wlist)

class de_bruijn_graph(object):

    def __init__(self, nodes, edges):
        ''' constructor '''
        self.dbgraph = {}
        self.nodes = nodes
        for e in edges:
            if e in self.dbgraph:
                self.dbgraph[e] += 1
            else:    
                self.dbgraph[e]  = 1
        self.odd = None        

    def is_eulirean(self):
        ''' does graph have a eulirean circuit/path '''
        if self.odd is None:
            odd = 0
            for k in self.dbgraph:
                if self.dbgraph[k] % 2 != 0:
                    odd += 1
                print k, self.dbgraph[k]
            self.odd = odd        
            print self.odd

        # not eulirean
        if self.odd > 2:        
            return 0

        # eulirean circuit    
        if self.odd == 0:
            return 1

        # eulirean path  
        return 2

    def start_node(self):
        ''' pick a node from the graph '''
        max_e = 0
        for kt in self.dbgraph.keys():
            if self.odd:
                if self.dbgraph[kt] % 2 and self.dbgraph[kt] > max_e:
                    max_e = self.dbgraph[kt]
                    max_n = kt[0]
                else:
                    continue
            else:
                return kt[0]
        return max_n

    def eulirean_walk(self, s= None):
        ''' prints the path '''
        stack = []
        curr = None
        if s is None:
            s = self.start_node()
        print 'start_node {}'.format(s)
        while True:
            added = False
            for st in self.dbgraph.keys():
                if s == st[0]:
                    if self.dbgraph[st] > 0:
                        print st, self.dbgraph[st]
                        self.dbgraph[st] -= 1
                        stack.append(s)
                        s = st[1]
                        added = True
                        break
            if added:
                curr = s
            else:    
                break

        if curr is not None:
            stack.append(curr)
        return stack

def de_bruijn_ize(st, k):
    ''' generate multinode graph of kmers '''
    edges = []
    nodes = set()

    for i in range(len(st) - k + 1):
        edges.append((st[i : i + k - 1], st[i + 1 : i + k]))
        nodes.add(st[i : i + k - 1])
        nodes.add(st[i + 1 : i + k])
    return nodes, edges    

def ssp_de_bruijn(nodes, edges):
    ''' driver function for building de bruijn graph for ssp problem formulation '''
    dbgraph = de_bruijn_graph(nodes, edges)
    if dbgraph.is_eulirean() or True:
        sss = ''
        for v in nodes:
            e_path = dbgraph.eulirean_walk(v)
            for s in e_path:
                sss = overlapped_string(sss, s)
            print 'ssp de_bruijn {}'.format(sss)
        return sss    
    else:
        print 'Graph is not eulirean'
        return None

#s = 'ACTGAGCTA'
#nodes, edges = de_bruijn_ize(s, 3)
#s = 'AABB'
#nodes, edges = de_bruijn_ize(s, 3)
#s = 'a_long_long_long_time'
#nodes, edges = de_bruijn_ize(s, 5)
s = 'ZABCDABEFABY'
nodes, edges = de_bruijn_ize(s, 3)
print ssp_de_bruijn(nodes, edges)

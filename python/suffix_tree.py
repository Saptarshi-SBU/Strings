#!/usr/bin/python
# suffix tree construction from suffix array

from lcp import LCP
from suffix_array import BuildSuffixArrayWithPrefixDouble

class SuffixNode(object):
    """
        A node in the suffix tree.
    """
    def __init__(self, parent, depth, suffix_pos):
        # up traversal during common ancestor finding
        self.parent = parent
        # common ancestor depth, set only for internal nodes
        self.depth = depth
        # suffix keys, only for internal nodes
        self.children = {}
        # suffix pos, only for leaf nodes
        self.suffix_pos = suffix_pos

    def isleaf(self):
        return self.suffix_pos >= 0

def CreateInternalSuffixNode(parent, depth):
    return SuffixNode(parent, depth, -1)

def CreateLeafSuffixNode(parent, suffix_pos):
    return SuffixNode(parent, 0, suffix_pos)

def CreateRootSuffixNode():
    return CreateInternalSuffixNode(None, 0)

class SuffixTree(object):
    """
        A suffix tree for string matching.
    """
    def __init__(self, case_insensitive=False):
        """
        string
            the string for which to construct a suffix tree
        """
        self.root = None
    
    def buildFromSuffixArray(self, string, suffix_array, lcp):
        """
            The core construction method.
        """
        lcp_prev = 0
        self.root = CreateRootSuffixNode()
        curr_node = self.root

        for i in range(len(suffix_array)):
            suffix_pos = suffix_array[i]

            print ('[{}]. SUFFIX string :{} begin_pos :{}'.format\
                (i, string[suffix_pos : len(string)], suffix_pos))

            # no common ancestor, an entirely new suffix
            if lcp_prev == 0:
                    curr_node = self.root
                    print ('==>using curr node keys : {} depth {} lcp {}'.format\
                        (curr_node.children.keys(), curr_node.depth, lcp_prev))
                    curr_node.children[string[suffix_pos]] = \
                        CreateLeafSuffixNode(curr_node, suffix_pos)
                    print ('suffix has no common ancestor')
            # has exactly the same common ancestor as last node
            elif lcp_prev == curr_node.depth:
                    print ('suffix has exact common ancestor')
                    print ('==>using curr node keys : {} depth {} lcp {}'.format\
                        (curr_node.children.keys(), curr_node.depth, lcp_prev))
                    curr_node.children[string[suffix_pos + lcp_prev]] = \
                        CreateLeafSuffixNode(curr_node, suffix_pos)
            # has common ancestor with a degree of similarity
            else:
                    print ('suffix has overlapping common ancestor')
                    # We can never reach None as current node in iteration
                    while curr_node.depth > lcp_prev:
                        assert curr_node.suffix_pos < 0
                        print ('suffix path curr node keys : {} depth {}'.format\
                            (curr_node.children.keys(), curr_node.depth))
                        curr_node = curr_node.parent
            
                    print ('==>using curr node keys : {} depth {} lcp {}'.format\
                        (curr_node.children.keys(), curr_node.depth, lcp_prev))

                    if lcp_prev == curr_node.depth:
                        curr_node.children[string[suffix_pos + lcp_prev]] = \
                            CreateLeafSuffixNode(curr_node, suffix_pos)
                    else:
                        # update old node
                        suffix_keys = sorted(curr_node.children.keys())
                        # suffix keys are sorted
                        suffix_key = suffix_keys[-1]
                        print ('suffix key :{}'.format(suffix_key))
                        old_node = curr_node.children[suffix_key]

                        curr_depth = curr_node.depth
                        # more to match
                        if lcp_prev > curr_depth:
                            new_intnode = None
                            while curr_depth < lcp_prev:
                                curr_depth = curr_depth + 1
                                new_intnode = CreateInternalSuffixNode(curr_node, curr_depth)
                                curr_node.children[string[suffix_pos + curr_depth - 1]] = new_intnode
                                curr_node = new_intnode
                                print ('suffix path new curr node keys : {} depth {}'.format\
                                    (curr_node.children.keys(), curr_node.depth))
                            assert new_intnode    
                        else:
                            new_intnode = CreateInternalSuffixNode(curr_node, curr_depth)
                            curr_node.children[suffix_key] = new_intnode
                            curr_node = new_intnode

                        old_node.parent = new_intnode
                        new_intnode.children[string[old_node.suffix_pos + lcp_prev]] = old_node
                        new_intnode.children[string[suffix_pos + lcp_prev]] = \
                                CreateLeafSuffixNode(new_intnode, suffix_pos)

            print ('<==updated curr node :{}'.format(curr_node.children.keys()))

            # additional 1 because of lcp dictionary keys
            if i < len(suffix_array) - 1:
                lcp_prev = lcp[i + 1 + 1]

        return

    def printSuffixTree(self, string):
        """
            Suffix tree inorder traversal
        """
        count = 0
        sorted_suffixes = []

        if self.root is None:
            return sorted_suffixes

        nodeStack = []
        # depth indices
        indexPositions = [0 for x in range(len(string)) ]
    
        print ('Printing suffix tree {}'.format(string))

        #depth index iterator
        curr_depth = 0
        nodeStack = [ self.root ]
        #print self.root.children.keys()
        while len(nodeStack) > 0:
            node = nodeStack[-1]
            length = len(node.children)
            if indexPositions[curr_depth] < length:
                keys = sorted(node.children.keys())
                #print keys
                node = node.children[keys[indexPositions[curr_depth]]]
                indexPositions[curr_depth] = indexPositions[curr_depth] + 1
                nodeStack.append(node)
                curr_depth = curr_depth + 1
            else:
                if node.isleaf():
                    suffix = string[node.suffix_pos : len(string)]
                    sorted_suffixes.append(suffix)
                    count = count + 1
                    print ('[{}] {}'.format(count, suffix))
                nodeStack.pop()
                indexPositions[curr_depth] = 0
                curr_depth = curr_depth - 1

        assert curr_depth < 0, "depth :%r" % curr_depth
        return sorted_suffixes
                
if __name__ == "__main__":
        text = "ACAGACTTTAGACT"
        suffix_array = BuildSuffixArrayWithPrefixDouble(text)
        #print suffix_array
        lcp = LCP(text, suffix_array)
        #print lcp
        text = text + '$'
        suffix_array.pop(0)
        suffix_tree = SuffixTree()
        suffix_tree.buildFromSuffixArray(text, suffix_array, lcp)
        suffix_tree.printSuffixTree(text)

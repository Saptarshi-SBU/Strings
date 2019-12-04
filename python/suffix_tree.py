#!/usr/bin/python
# suffix tree construction from suffix array

from suffix_array import BuildSuffixArrayWithPrefixDouble, LCP

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
    
    def __repr__(self):
        """ 
        Lists children in the suffix tree
        """
            
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
                        new_intnode = CreateInternalSuffixNode(curr_node, lcp_prev)

                        # update old node
                        suffix_keys = sorted(curr_node.children.keys())
                        # suffix keys are sorted
                        suffix_key = suffix_keys[-1]
                        #print ('suffix key :{}'.format(suffix_key))
                        old_node = curr_node.children[suffix_key]
                        old_node.parent = new_intnode

                        # update linkages
                        curr_node.children[suffix_key] = new_intnode
                        new_intnode.children[string[old_node.suffix_pos + lcp_prev]] = old_node
                        new_intnode.children[string[suffix_pos + lcp_prev]] = \
                            CreateLeafSuffixNode(new_intnode, suffix_pos)
                        curr_node = new_intnode

            print ('<==updated curr node :{}'.format(curr_node.children.keys()))

            # additional 1 because of lcp dictionary keys
            if i < len(suffix_array) - 1:
                lcp_prev = lcp[i + 1 + 1]

        return

    def printSuffixTree(self, string):
        """
            Suffix tree inorder traversal
        """
        sorted_suffixes = []

        if self.root is None:
            return sorted_suffixes

        nodeStack = []
        # depth indices
        indexPositions = [0 for x in range(len(string)) ]
    
        print ('Printing suffix tree')

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
                    print (suffix)
                nodeStack.pop()
                indexPositions[curr_depth] = 0
                curr_depth = curr_depth - 1

        assert curr_depth < 0, "depth :%r" % curr_depth
        return sorted_suffixes
                
#string = "ACTAGAGACTTTAGACT"
#suffix_array2 = [14, 0, 7, 12, 5, 3, 15, 1, 8, 13, 6, 4, 16, 11, 2, 10, 9]
#lcp = {1: 0, 2: 3, 3: 3, 4: 1, 5: 5, 6: 3, 7: 0, 8: 2, 9: 2, 10: 0, 11: 4, 12: 2, 13: 0, 14: 1, 15: 4, 16: 1, 17: 2}
if __name__ == "__main__":
    #string = "ACTAGAGACTTTAGACT"
    #string = "ACAGACTTTAGACT"
    string = "ACAACTTACT"
    suffix_array = BuildSuffixArrayWithPrefixDouble(string)
    lcp = LCP(string, suffix_array)
    print suffix_array
    print lcp
    string = string + '$'
    suffix_array.pop(0)
    suffix_tree = SuffixTree()
    suffix_tree.buildFromSuffixArray(string, suffix_array, lcp)
    suffix_tree.printSuffixTree(string)

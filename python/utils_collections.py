#!/usr/bin/python
#
#  collection of utility recipes
#

def permutation(nr, ans, ilist=[]):
    ''' returns permutation of indices '''
    #base
    if len(ilist) == nr:
        # cannot do ans.append(ilist) since ilist is pushed as reference whose content changes
        # ref : https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
        ans.append([ x for x in ilist])
        return

    # choose unique element
    for i in range(nr):
        if i in ilist:
            continue
        ilist.append(i)
        permutation(nr, ans, ilist)
        ilist.pop(-1)

def overlapped_string(p, q):
    ''' returns a string overlapping p and q '''
    i = j = 0
    np = len(p)
    nq = len(q)

    for j in reversed(range(nq)):
        match = False
        i = np - 1
        while i >= 0 and j >= 0:
            if p[i] == q[j]:
                i = i - 1
                j = j - 1
                match = True
            else:
                break

        if match is True and j < 0:
            return p[0 : i + 1] + q

    return p + q        

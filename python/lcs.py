#!/usr/bin/python

# alignment based on longest common subsequence

class LCS(object):

    def __init__(self, textp, textq):
        self.textp = textp
        self.textq = textq
       
    def lcs(self, i, M, j, N):
        if i >= M or j >= N:
            return 0

        # On character match, we increase lcs, extend the text and pattern for remaining subsequence
        l1 = 0
        if self.textp[i] == self.textq[j]:
            l1 = 1 + self.lcs(i + 1, M, j + 1, N)

        # Also, explore other candidate subsequences, skipping the current character in text or/pattern
        # We do not want to miss a larger subsequence by matching it early in text and getting exhausted
        # when there can be a larger subsequence possible if we skipped the match. E.g. See test cases
        l2 = max((self.lcs(i + 1, M, j, N), self.lcs(i, M, j + 1, N)))

        return max(l1, l2)

    def length(self):
        return self.lcs(0, len(textp), 0, len(textq))

textp = "algoritghgr"
textq = "grithm"
print 'lcs {}'.format(LCS(textp, textq).length())

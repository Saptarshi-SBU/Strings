#!/usr/bin/python

# alignment based on longest common subsequence

class LCS(object):

    def __init__(self, textp, textq):
        self.textp = textp
        self.textq = textq
       
    def lcs(self, i, M, j, N):
        l = 0
        s = []
        if i >= M or j >= N:
            return l, s

        # On character match, we increase lcs, extend the text and pattern for remaining subsequence
        l1 = 0
        if self.textp[i] == self.textq[j]:
            l1, s1 = self.lcs(i + 1, M, j + 1, N)
            s1.append((i, j))
            l = l1 + 1
            s = s1

        # Also, explore other candidate subsequences, skipping the current character in text or/pattern
        # We do not want to miss a larger subsequence by matching it early in text and getting exhausted
        # when there can be a larger subsequence possible if we skipped the match. E.g. See test cases
        l2, s2 = self.lcs(i + 1, M, j, N)
        if l2 > l:
            l = l2
            s = s2

        l3, s3 = self.lcs(i, M, j + 1, N)
        if l3 > l:
            l = l3
            s = s3

        #print l1, l2, l3, s
        assert s is not None
        return l, s

    def lcsDP(self):
        
        M = len(self.textp)
        N = len(self.textq)
        s = []

        D = [ [] for x in range(N + 1) ]
        for i in range(N + 1):
            D[i] = [ 0 ] * (M + 1)
    
        for i in reversed(range(N)):
            for j in reversed(range(M)):
                d1 = D[i][j + 1]
                d2 = D[i + 1][j]
                if self.textp[j] == self.textq[i]:
                    d3 = 1 + D[i + 1][j + 1] 
                else:
                    d3 = 0
                D[i][j] = max(d1, d2, d3)

        #print sequence
        #D matrix is kind of triangular in nature. We use the lcs sum
        #property to find subsequence characters part of the length.
        #for d in D:        
        #    print d     

        lcs = D[0][0]
        for i in range(N):
            if lcs <= 0:
               break

            #if there are no matches in a row which contributes to max lcs,
            #there will be no transition, otherwise we will see a step-down.
            for j in range(M):
               if D[i][j] < lcs:
                   assert j > 0
                   s.append(j - 1)
                   lcs = lcs - 1
                   break
               #boundary case    
               if i == N - 1 and j == M - 1 and lcs and D[i][j] == lcs:    
                   s.append(j)
                   lcs = lcs - 1
                   break
                
        return D[0][0], s

    def length(self):
        return self.lcs(0, len(self.textp), 0, len(self.textq))[0]

    def sequence(self):
        l, p = self.lcs(0, len(self.textp), 0, len(self.textq))
        a = ['-' for x in range(len(self.textp)) ]
        for tp in p:
            a[tp[0]] = self.textp[tp[0]]
        return l, ''.join(a)

    def sequenceDP(self):
        l, p = self.lcsDP()
        a = ['-' for x in range(len(self.textp)) ]
        for tp in p:
            a[tp] = self.textp[tp]
        return l, ''.join(a)


if __name__ == "__main__":
    textp = "aaaaaabbbcd"
    textq = "abc"
    l = LCS(textp, textq).length()
    print 'lcs {}'.format(l)
    l, texta = LCS(textp, textq).sequence()
    print 'textp: {}'.format(textp)
    print 'texta: {}'.format(texta)
    l, texta = LCS(textp, textq).sequenceDP()
    print 'lcs {}'.format(l)
    print 'textp: {}'.format(textp)
    print 'texta: {}'.format(texta)

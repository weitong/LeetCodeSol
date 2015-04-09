#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        def naive(S):
            ss = []
            S.sort()
            size = len(S)
            for j in range(2**size):
                s = []
                for i in range(size):
                    if (j >> i ) & 1:
                        s.append(S[i])
                ss.append(s)
            return ss
        return naive(S)
if __name__ == "__main__":
    sol = Solution()
    print sol.subsets([1,2,3])

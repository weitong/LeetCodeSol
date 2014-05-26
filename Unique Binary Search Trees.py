#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @return an integer
    def numTrees(self, n):
        def rec(f, t):
            if f >= t:
                return 1
            else:
                tsum = 0
                for i in range(f, t + 1):
                    tsum += (rec(f, i-1) * rec(i+1, t))
                return tsum
        return rec(1, n)
    
if __name__ == "__main__":
    sol = Solution()
    print sol.numTrees(2)
    print sol.numTrees(3)

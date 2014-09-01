#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        mapping = [0, 1, 2] + [0] * (n - 2)
        for i in range(3, n + 1):
            mapping[i] = mapping[i-1] + mapping[i-2]
        return mapping[n]
	
		

#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result

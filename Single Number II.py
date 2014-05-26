#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bit_array = [0] * 33
        for i in A:
            cur = i
            if i < 0:
                bit_array[32] += 1
                cur = -i
                
            for pos in range(32):
                bit = (cur >> pos) % 2
                bit_array[pos] += bit
        
        for pos in range(33):
            bit_array[pos] %= 3
        
        result = 0
        for pos in range(32):
            result += bit_array[pos] * (2 ** pos)
        
        if bit_array[32] == 1:
            return -result
        else:
            return result

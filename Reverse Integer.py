#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#


class Solution:
    # @return an integer
    def reverse(self, x):
        signal = 1
        if x < 0:
            signal = -1
            x = -x
        
        revn = 0
        while x > 0:
            revn = revn * 10 + x % 10
            x = int(x // 10)
        
        return signal * revn
    

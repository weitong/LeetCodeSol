#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        delta = []
        for i in range(1, len(prices)):
            delta.append(prices[i] - prices[i-1])
        
        msum = 0
        for d in delta:
            if d > 0:
                msum += d
        
        return msum

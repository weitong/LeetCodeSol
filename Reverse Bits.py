#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[::-1][:-2]
        return int(b + (32 - len(b)) * '0', 2)
        
        
if __name__ == "__main__":
    sol = Solution()
    print sol.reverseBits(43261596)

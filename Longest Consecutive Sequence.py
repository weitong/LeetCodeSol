#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        seq = {}
        longest = 0
        for i in num:
            if i not in seq:
                lower, upper = i, i
                if i - 1 in seq:
                    lower = seq[i - 1]
                if i + 1 in seq:
                    upper = seq[i + 1]
                longest = max(longest, (upper - lower) + 1)
                seq[i], seq[lower], seq[upper]  = i, upper, lower
        return longest
        
if __name__ == "__main__":
    sol = Solution()
    print sol.longestConsecutive([100, 4, 200, 1, 3, 2])
    

#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        number = 0
        base = ord('A') - 1
        for i in range(len(s)):
            number = number * 26 + (ord(s[i]) - base)
        return number
        
if __name__ == "__main__":
    sol = Solution()
    print sol.titleToNumber('C')
    print sol.titleToNumber('AA')
    print sol.titleToNumber('ZZ')
    print sol.titleToNumber('AAA')

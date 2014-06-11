#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        sl = s.split(' ')
        tsl = []
        for w in sl:
            if w != ' ' and w != '':
                tsl.append(w)
        #print tsl
        if len(tsl) == 0:
            return 0
        else:
            return len(tsl[-1])
if __name__ == "__main__":
    sol = Solution()
    print sol.lengthOfLastWord("Hello World")
    print sol.lengthOfLastWord("Hello World   ")
    print sol.lengthOfLastWord("Hello      World")
    print sol.lengthOfLastWord("      ")

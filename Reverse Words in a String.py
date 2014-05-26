#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        tmp1 = s.split(" ")
        tmp2 = []
        for i in reversed(tmp1):
            if i != " " and i != "":
                tmp2.append(i)
                
        if len(tmp2) == 0:
            return ""
        else:
            return ' '.join(tmp2)

#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        

        result = ''
        for i in xrange(min([len(s) for s in strs])):
            c = strs[0][i]
            whoops = True
            for s in strs[1:]:
                if s[i] != c:
                    whoops = False
                    break
            if whoops:
                result += c
            else:
                break
        return result

if __name__ == "__main__":
    
    
    sol = Solution()
    print sol.longestCommonPrefix([])
    print sol.longestCommonPrefix(['ansc'])
    print sol.longestCommonPrefix(['abac', 'abcdef'])
    print sol.longestCommonPrefix(['abcd', 'eeee'])
    print sol.longestCommonPrefix(['ansc', 'anscccc', 'an'])
    print sol.longestCommonPrefix(['ansc', 'anscccc', ''])

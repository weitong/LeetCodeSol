#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#
class Solution:
    # @return a boolean
    def isValid(self, s):
        l = {'(': 1, '{': 2, '[': 3}
        r = {')': 1, '}': 2, ']': 3}
        stack = []
        for i in range(len(s)):
            if s[i] in l.keys():
                stack.append(s[i])
            elif s[i] in r.keys():
                if len(stack) == 0:
                    return False
                
                e = stack[-1]
                del(stack[-1])
                if l[e] != r[s[i]]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                    
                
        
if __name__ == "__main__":
    sol = Solution()
    print sol.isValid("(([])")

#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                del(A[i])
        return len(A)

if __name__ == "__main__":
    sol = Solution()

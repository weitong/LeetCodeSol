#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        nhere, nmaxi = A[0], A[0]
        for i in range(1, len(A)):
            if nhere <= 0:
                nhere = A[i]
            else:
                nhere += A[i]
                
            if nhere > nmaxi:
                nmaxi = nhere
        return nmaxi


# divide and conquer 
class DCSolution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        

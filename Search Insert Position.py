#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if i == 0:
                if target <= A[0]:
                    return 0
            else:
                if A[i] >= target > A[i-1]:
                    return i
        return len(A)


if __name__ == "__main__":
    sol = Solution()
    print sol.searchInsert([1,3,5,6], 5)
    print sol.searchInsert([1,3,5,6], 2)
    print sol.searchInsert([1,3,5,6], 7)
    print sol.searchInsert([1,3,5,6], 0)
    

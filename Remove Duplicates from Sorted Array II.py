#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n < 3:
            return n
        ball = hole = 2
        while ball < n:
            if A[ball] != A[hole-2]:
                A[hole] = A[ball]
                hole += 1
            ball += 1
                    
                    
        return hole

if __name__ == "__main__":
    A = [1,1,1,2,2,3]
    sol = Solution()
    a = sol.removeDuplicates(A)
    print a, A[0:a] 

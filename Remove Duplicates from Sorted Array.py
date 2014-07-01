#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#
    
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 1:
            return length
        
        cur = A[0]
        i = 1
        k = 1
        while i < length:
            j = i
            while j < length and cur == A[j]:
                j += 1

            if j == length:
                break
            
            A[k] = A[j]
            k += 1
            i = j
            cur = A[i]
        A = A[0:k]
        return k
    

class Solution1:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 1:
            return length
        
        cur = A[0]
        i = 1
        while i < length:
            if cur == A[i]:
                del(A[i])
                length -= 1
            else:
                cur = A[i]
            i += 1
        return len(A)

if __name__ == "__main__":
    sol = Solution()
    A = [1,1,2, 2, 2, 3, 4, 4, 5, 6,6,6,6,7]
    print sol.removeDuplicates(A)
    print A

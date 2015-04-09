#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        length = len(A)
        def solution1():
            h, t = 0, length - 1         
            while t - h > 1:
                p = int((h + t) / 2)
                if A[h] < A[t]:
                    if target > A[p]:
                        h = p
                    elif target < A[p]:
                        t = p
                    else:
                        return p
                else:
                    if target == A[p]:
                        return p
                    elif target > A[p]:
                        if target <= A[t]:
                            h = p
                        else:
                            if A[p] > A[h]:
                                h = p
                            else:
                                t = p
                    else:
                        if target >= A[h]:
                            t = p
                        else:
                            if A[p] > A[h]:
                                h = p
                            else:
                                t = p
            if target == A[h]:
                return h
            elif target == A[t]:
                return t
            else:
                return -1

        def solution2():
            # find the peak than binary
            def peak(num):
                length = len(num)
                if length == 1:
                    return 0

                if num[0] > num[1]:
                    return 0

                if num[length-1] > num[length-2]:
                    return length-1

                h, t = 0, length-1 
                while h != t:
                    p = int((h + t) / 2)
                    if num[p] > num[p-1]:
                        if num[p] > num[p+1]:
                            return p
                        else:
                            h = p
                    else:
                        t = p
                return h

            
            pass
            
        return solution1()

if __name__ == "__main__":
    sol = Solution()
    a = [4, 5, 2, 3]

    for i in a:
        print sol.search(a, i)

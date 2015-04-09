#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#
import random

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        def naiveSolution(num):
            length = len(num)
            if length == 1:
                return 0
            
            if num[0] > num[1]:
                return 0
            
            for i in range(1, length-1):
                if num[i] > num[i+1] and num[i] > num[i-1]:
                    return i

            return length - 1
    
        def linearTimeSolution(num):
            length = len(num)
            if length == 1:
                return 0
            
            if num[0] > num[1]:
                return 0
            i = 1
            while i < length - 1:
                if num[i] > num[i+1]:
                    return i
                i += 1
            return length - 1
                    

        def logTimeSolution(num):
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
            
        return linearTimeSolution(num), logTimeSolution(num)
    
if __name__ == "__main__":
    t1 = [1, 2, 3, 1]
    t2 = [1, 2, 3, 4, 5, 1]
    t3 = [1, 2, 8, 4, 5, 1]
    t4 = [1, 9, 3, 4, 8, 1]
    t5 = [1, 2, 3, 4, 5, 1, 4, 9, 3, 4, 8, 1]
    
    testcase = [t1, t2, t3, t4, t5]
    sol = Solution()

    for t in testcase:
        print sol.findPeakElement(t)
    

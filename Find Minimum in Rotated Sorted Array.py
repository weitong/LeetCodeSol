#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class NaiveSolution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        min = num[0]
        for i in num[1:]:
            if i < min:
                return i
        return min

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        p, q = 0, len(num) - 1
        while q - p > 1:
            current = int((p + q) / 2)
            if num[current] > num[p] and num[current] > num[q]:
                p = current + 1
            else:
                q = current

        if p == q:
            return num[p]
        else:
            return min(num[p], num[q])
        

if __name__ == "__main__":
    sol = Solution()
    print sol.findMin([0])

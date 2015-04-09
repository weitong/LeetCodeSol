#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        major = num[0]
        count = 1
        for i in range(1, len(num)):
            if count == 0:
                count += 1
                major = num[i]
            elif major == num[i]:
                count += 1
            else:
                # key step, use the other elements to beat the current major.
                count -= 1
        return major
            

if __name__ == "__main__":
    sol = Solution()

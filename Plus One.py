#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        i = len(digits) - 1
        while True:
            if digits[i] != 9:
                break
            else:
                digits[i] = 0
            i -= 1
                
        if i == -1:
            digits.append(0)
            digits[0] = 1
        else:
            digits[i] += 1

        return digits
    
if __name__ == "__main__":
    sol = Solution()
    print sol.plusOne([9])
    print sol.plusOne([9, 2, 5])
    print sol.plusOne([9, 9, 9, 9])
    print sol.plusOne([9, 4, 5, 9, 9])
    print sol.plusOne([0])

#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target < row[0]:
                return False
            elif target > row[-1]:
                continue
            else:
                for item in row:
                    if target < item:
                        return False
                    elif target == item:
                        return True
                    else:
                        pass
        return False


if __name__ == "__main__":
    sol = Solution()
    a = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print sol.searchMatrix(a, 3)
    print sol.searchMatrix(a, 16)
    print sol.searchMatrix(a, 33)

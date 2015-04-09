#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        mtx = []
        for i in range(n):
            mtx.append([0] * n)
        i, j, num = 0, 0, 1
        mtx[0][0] = 1
        direction = 'R'
        while (i != n / 2) or (j != (n - 1) / 2):
            if i == 0 and j == 0:
                j += 1
                direction = 'R'
            elif i + j == n - 1:
                if i <= j:
                    i += 1
                    direction = 'D'
                else:
                    i -= 1
                    direction = 'U'
            elif i == j and i >= n / 2:
                j -= 1
                direction = 'L'
            elif i - j == 1 and i <= n / 2:
                j += 1
                direction = 'R'
            else:
                if direction == 'R':
                    j += 1
                elif direction == 'L':
                    j -= 1
                elif direction == 'U':
                    i -= 1
                else:
                    i += 1
            num += 1
            mtx[i][j] = num
        return mtx
                
         
if __name__ == "__main__":
    sol = Solution()
    for i in sol.generateMatrix(4):
        print i

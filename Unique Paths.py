#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        
        blocks = []
        for i in range(m):
            blocks.append([0] * n)

        s = m + n - 2
        blocks[m - 1][n - 1] = 1
        for si in range(s - 1, 0, -1):
            i = min(si, m - 1)
            while True:
                j = si - i
                if i == m - 1:
                    blocks[i][j] = blocks[i][j + 1]
                elif j == n - 1:
                    blocks[i][j] = blocks[i + 1][j]
                else:
                    blocks[i][j] = blocks[i][j + 1] + blocks[i + 1][j]

                if j == n - 1 or i == 0:
                    break
                i -= 1
                
        return blocks[1][0] + blocks[0][1]
                    
if __name__ == "__main__":
    sol = Solution()
    print sol.uniquePaths(6, 2)

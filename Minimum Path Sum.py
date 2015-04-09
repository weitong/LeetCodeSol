#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        if m == 1:
            return sum(grid[0])
        elif n == 1:
            return sum([col[0] for col in grid])
        
        blocks = []
        for i in range(m):
            blocks.append([0] * n)

        s = m + n - 2
        blocks[m - 1][n - 1] = grid[m - 1][n - 1]
        for si in range(s - 1, 0, -1):
            i = min(si, m - 1)
            while True:
                j = si - i
                if i == m - 1:
                    blocks[i][j] = blocks[i][j + 1] + grid[i][j]
                elif j == n - 1:
                    blocks[i][j] = blocks[i + 1][j] + grid[i][j]
                else:
                    blocks[i][j] = min(blocks[i][j + 1], blocks[i + 1][j]) + grid[i][j]
                    
                if j == n - 1 or i == 0:
                    break
                i -= 1
                
        return min(blocks[1][0], blocks[0][1]) + grid[0][0]
                    
if __name__ == "__main__":
    sol = Solution()
    print sol.minPathSum([[1, 2, 7, 8], [2, 5, 9, 10]])

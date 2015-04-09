#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        if m == 1:
            for b in obstacleGrid[0]:
                if b == 1:
                    return 0
            return 1
        elif n == 1:
            for col in obstacleGrid:
                if col[0] == 1:
                    return 0
            return 1
        
        
        blocks = []
        for i in range(m):
            blocks.append([0] * n)

        s = m + n - 2
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        else:
            blocks[m - 1][n - 1] = 1
            
        for si in range(s - 1, 0, -1):
            i = min(si, m - 1)
            while True:
                j = si - i
                if obstacleGrid[i][j] == 1:
                    blocks[i][j] = 0
                else:
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
    print sol.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])

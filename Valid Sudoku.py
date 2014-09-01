#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isValid(cell):
            cell = filter(lambda a: a != '.', cell)
            return len(cell) == len(set(cell))

        for i in range(9):
            cell = {}
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    if cur in cell:
                        return False
                    else:
                        cell[board[i][j]] = True

        for j in range(9):
            cell = {}
            for i in range(9):
                cur = board[i][j]
                if cur != '.':
                    if cur in cell:
                        return False
                    else:
                        cell[board[i][j]] = True
                

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                cell = {}
                
                for k in board[i][j:j+3] + board[i + 1][j:j+3] + board[i + 2][j:j+3]:
                    if k != '.':
                        if k in cell:
                            return False
                        else:
                            cell[k] = True
        return True

"""
A more efficient Method
public boolean isValidSudoku(char[][] board) {
    int row, row2;
    int col, col2;
    int sqr, sqr2;
    int a,b,c;

    for(int i=0;i<9;i++){
        row = 0; row2 = 0;
        col = 0; col2 = 0;
        sqr = 0; sqr2 = 0;
        for(int j=0;j<9;j++){
            a = board[i][j] - '0';                      // columns
            b = board[j][i] - '0';                      // rows
            c = board[3*(i%3)+j/3][3*(i/3)+j%3] -'0';   // sections
            if(a>0) row2 ^= 1 << a;
            if(b>0) col2 ^= 1 << b;
            if(c>0) sqr2 ^= 1 << c;

            if(row2 < row || col2 < col || sqr2 < sqr) 
                return false;
            row = row2;
            col = col2;
            sqr = sqr2;
        }
    }
    return true;
}
"""

if __name__ == "__main__":
    sudoku = [
        [5, 3, '.', '.', 7, '.', '.', '.', '.'],
        [6, '.', '.', 1, 9, 5, '.', '.','.'],
        ['.', 9, 8, '.', '.','.', '.', 6, '.'],
        [8, '.', '.', '.', 6, '.', '.', '.', 3],
        [4, '.', '.', 8, '.', 3, '.', '.', 1],
        [7, '.', '.', '.', 2, '.', '.', '.', 6],
        ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
        ['.', '.', '.', 4, 1, 9, '.', '.', 5],
        ['.', '.', '.', '.', 8, '.', '.', 7, 9]]
    sol = Solution()
    print sol.isValidSudoku(sudoku)
                

#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 36_valid_sudoku
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def isValidSudoku(self, board):
        #分别比较行、列、九宫格
        for i in range(9):
            d_row = {}
            d_col = {}
            d_mat = {}
            for j in range(9):
                if ((board[i][j] in d_row and board[i][j] != '.') or (board[j][i] in d_col and board[j][i] != '.') or
                    (board[i - i%3 + j//3][i%3 * 3 + j%3] in d_mat and board[i - i%3 + j//3][i%3 * 3 + j%3] != '.')):
                    return False
                else:
                    d_row[board[i][j]] = 1
                    d_col[board[j][i]] = 1
                    d_mat[board[i - i%3 + j//3][i%3 * 3 + j%3]] = 1
        return True


    def isValidSudoku2(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i//3,j//3,c)]
        return len(seen) == len(set(seen))


board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

solute = Solution()
res = solute.isValidSudoku2(board)

print(res)
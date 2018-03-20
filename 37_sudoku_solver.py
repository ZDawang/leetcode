#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-26
#difficulty degree：
#problem: 37_sudoku_solver
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
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

    def solve(self, board, d):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                for k in d[str(i) + str(j)]:
                    board[i] = board[i][:j] + str(k) + board[i][j + 1:]
                    if self.isValidSudoku(board) and self.solve(board, d):
                        return True
                    board[i] = board[i][:j] + '.' + board[i][j + 1:]
                return False
        return True

    def solveSudoku(self, board):
        #先优化以减少运算量
        row_lack = [[str(j) for j in range(1,10)] for i in range(9)]
        col_lack = [[str(j) for j in range(1,10)] for i in range(9)]
        mat_lack = [[str(j) for j in range(1,10)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    row_lack[i].remove(board[i][j])
                    col_lack[j].remove(board[i][j])
                    mat_lack[i - i %3 + j // 3].remove(board[i][j])
                except:
                    pass
        test = 0
        d = {}
        while row_lack:
            if board == test:
                break
            test = board
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        d[str(i) + str(j)] = []
                        k = 0
                        for num in row_lack[i]:
                            if num in col_lack[j] and num in mat_lack[i - i %3 + j // 3]:
                                d[str(i) + str(j)].append(num)

        self.solve(board, d)




class Solution:
    def solveSudoku(self, board):
        def dfs(i, j):
            if j >= 9:
                return True
            if board[i][j] != ".":
                return dfs((i + 1)%9, j + (i + 1)//9)
            for c in str_nums:
                if (i, c) in d_row or (j, c) in d_col or (i//3, j//3, c) in d_mat:
                    continue
                board[i][j] = c
                d_row.add((i, c))
                d_col.add((j, c))
                d_mat.add((i//3, j//3, c))
                if dfs((i + 1)%9, j + (i + 1)//9):
                    return True
                board[i][j] = "."
                d_row.remove((i, c))
                d_col.remove((j, c))
                d_mat.remove((i//3, j//3, c))
            return False

        str_nums = [str(i) for i in range(1, 10)]
        d_row, d_col, d_mat = set(), set(), set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                d_row.add((i, board[i][j]))
                d_col.add((j, board[i][j]))
                d_mat.add((i//3, j//3, board[i][j]))
        return dfs(0, 0)

            
            

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

solute = Solution()
solute.solveSudoku(board)

print(board)
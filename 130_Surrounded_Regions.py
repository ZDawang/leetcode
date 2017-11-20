#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 130_Surrounded_Regions.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #通过BFS，查看是否有出去的O，同时使用集合记录已经查看过的点,并记录所有可以出去的O
    #TLE
    def solve(self, board):
        if not board: return
        m, n = len(board), len(board[0])
        d = set()
        queue = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" or (i, j) in d:
                    continue
                queue.append((i, j))
                state = False
                list_remove = []
                while queue:
                    posx, posy = queue.pop(0)
                    list_remove.append((posx, posy))
                    d.add((posx, posy))
                    if posx == 0 or posx == m - 1 or posy == 0 or posy == n - 1:
                        state = True
                    if posx != 0 and board[posx - 1][posy] == "O" and not (posx - 1, posy) in d: queue.append((posx - 1, posy))
                    if posx != m - 1 and board[posx + 1][posy] == "O" and not (posx + 1, posy) in d: queue.append((posx + 1, posy))
                    if posy != 0 and board[posx][posy - 1] == "O" and not (posx, posy - 1) in d: queue.append((posx, posy - 1))
                    if posy != n - 1 and board[posx][posy + 1] == "O" and not (posx, posy + 1) in d: queue.append((posx, posy + 1))
                if state == False:
                    for posx, posy in list_remove:
                        board[posx][posy] = "X"

    #遍历边界的"O"，将所有可以出去的O记录为"R",再做处理
    def solve(self, board):
        if not board: return
        m, n = len(board), len(board[0])
        queue = []
        for i in range(m):
            if board[i][0] == "O": queue.append((i, 0))
            if board[i][n - 1] == "O": queue.append((i, n - 1))
        for j in range(n):
            if board[0][j] == "O": queue.append((0, j))
            if board[m - 1][j] == "O": queue.append((m - 1, j))

        while queue:
            posx, posy = queue.pop(0)
            if posx >=0 and posx < m and posy >= 0 and posy < n and board[posx][posy] == "O":
                board[posx][posy] = "R"
                queue.append((posx - 1, posy))
                queue.append((posx + 1, posy))
                queue.append((posx, posy - 1))
                queue.append((posx, posy + 1))
        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "R" else "X"








board = ["XXXX","XOOX","XXOX","XOXX"]
solute = Solution()
res = solute.solve(board)




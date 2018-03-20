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

    #并查集，将所有O的指向边界的O,最后将所有不能指向边界的O全部标为X
    def solve3(self, board):
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            x, y = find(x), find(y)
            i, j = divmod(x, n)
            #若x为边界
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                uf[y] = x
            else:
                uf[x] = y

        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        uf = [i*n+j for i in range(m) for j in range(n)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i < m-1 and board[i + 1][j] == "O":
                        union(i*n+j, (i+1)*n+j)
                    if j < n-1 and board[i][j + 1] == "O":
                        union(i*n+j, i*n+j+1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    pos = find(i*n + j)
                    posi, posj = divmod(pos, n)
                    #若pos不是边界
                    if not (posi == 0 or posi == m-1 or posj == 0 or posj == n-1):
                        board[i][j] = "X"




board = ["XXXX","XOOX","XXOX","XOXX"]
solute = Solution()
res = solute.solve(board)




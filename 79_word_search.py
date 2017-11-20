#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 79_word_search
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def exist(self, board, word):
        def dfs(loc_x, loc_y, board, word, path, res):
            if res:
                return
            if loc_x < 0 or loc_y < 0 or loc_x >= len(board) or loc_y >= len(board[0]):
                return
            if [loc_x, loc_y] in path:
                return
            if board[loc_x][loc_y] == word[0]:
                if len(word) == 1:
                    res.append(1)
                    return
                else:
                    dfs(loc_x + 1, loc_y, board, word[1:], path + [[loc_x, loc_y]] , res)
                    dfs(loc_x - 1, loc_y, board, word[1:], path + [[loc_x, loc_y]] , res)
                    dfs(loc_x, loc_y + 1, board, word[1:], path + [[loc_x, loc_y]] , res)
                    dfs(loc_x, loc_y - 1, board, word[1:], path + [[loc_x, loc_y]] , res)
            else:
                return
        if not board:
            return False
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, board, word, [], res)
        return True if res else False




board = ["ABCE","SFCS","ADEE"]
word = "ABC"

solute = Solution()
res = solute.exist(board, word)
print(res)
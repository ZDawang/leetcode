#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 419_Battleships_in_a_Board.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #因为每两艘船之间至少有一个间隙，所以用找到一个X，上边跟左边不是X的话，就说明是一个新船。
    def countBattleships(self, board):
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    res += (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == ".")
        return res
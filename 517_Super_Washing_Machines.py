#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 517_Super_Washing_Machines
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #理解错题意，题意是任意m个机器，并且任意方向。理解为只能选一个方向
    def findMinMoves(self, machines):
        l = len(machines)
        dressnums = sum(machines)
        if dressnums % l != 0:
            return -1
        dressnum = dressnums // l
        move = []
        count = 0
        for i in range(l):
            count += machines[i]
            move.append((i + 1)*dressnum - count)
        res = abs(move[0])
        for i in range(1, l):
            if move[i] * move[i - 1] > 0:
                if abs(move[i]) > abs(move[i - 1]):
                    res += abs(move[i]) - abs(move[i - 1])
            else:
                res += abs(move[i])
        return res

    #使用move数组来表示每个机器需要向右传送衣服的数量。当小于0时，说明需要从右边传送给它
    #可以优化为O1
    def findMinMoves2(self, machines):
        l = len(machines)
        dressnums = sum(machines)
        if dressnums % l != 0:
            return -1
        dressnum = dressnums // l
        move = []
        count = 0
        for i in range(l):
            count += machines[i]
            move.append((i + 1)*dressnum - count)
        res = abs(move[0])
        for i in range(1, l):
            if move[i] < 0:
                res = max(res, abs(move[i]), abs(move[i - 1]), abs(move[i] - move[i - 1]))
            else:
                res = max(res, abs(move[i]), abs(move[i - 1]))
        return res

    def findMinMoves3(self, machines):
        l = len(machines)
        dressnums = sum(machines)
        if dressnums % l != 0:
            return -1
        avg = dressnums // l
        res = 0
        left = 0
        for i in range(l):
            right = machines[i] - avg - left
            res = max(res, left, right, left + right)
            left = -right
        return res


machines = [0,3,0]
solute = Solution()
res = solute.findMinMoves(machines)

print(res)

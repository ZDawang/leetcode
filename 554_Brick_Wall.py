#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 554_Brick_Wall
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #找出每行sum值都会取的最大个数
    def leastBricks(self, wall):
        d = {}
        for w in wall:
            wblock = 0
            for block in w:
                wblock += block
                d[wblock] = d.get(wblock, 0) + 1
        d[sum(wall[0])] = 0
        return len(wall) - max(d.values())

wall = [[1], [1], [1]]

solute = Solution()
res = solute.leastBricks(wall)
print(res)
#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 554_Brick_Wall
#time_complecity:  
#space_complecity: 
#beats: 
import collections
from functools import reduce
class Solution(object):
    #第一思路，扫描线。从左到右扫描。
    #m = len(wall), n = sum(wall[0])
    #时间复杂度O(mn),空间复杂度O(m),肯定会超时。。

    #哈希解法，将每行的cumsum都放入字典中。
    #则每个值的出现次数，则说明有多少行的wall都会在这里有间隙，取值出现的最大次数即可。
    def leastBricks(self, wall):
        if not wall: return 0
        d = collections.defaultdict(int)
        for w in wall:
            cumsum = 0
            for block in w:
                cumsum += block
                d[cumsum] += 1
        #不能包括wall的边缘。
        d[sum(wall[0])] = 0
        return len(wall) - max(d.values())


wall = [[1], [1], [1]]

solute = Solution()
res = solute.leastBricks(wall)
print(res)
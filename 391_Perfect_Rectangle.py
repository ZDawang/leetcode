#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 391_Perfect_Rectangle.py
#time_complecity:  
#space_complecity: 
#beats: 

from collections import defaultdict
class Solution(object):
    #所有范围的总和应该等于最终结果
    #每个顶点只应该出现2次或者4次
    #最终方形的顶点，只应该出现1次
    def isRectangleCover(self, rectangles):
        sums, corner = 0, set()
        L, R, U, D = float("inf"), float("-inf"), float("inf"), float("-inf")
        for rec in rectangles:
            L, R, U, D = min(L, rec[0]), max(R, rec[2]), min(U, rec[1]), max(D, rec[3])
            sums += (rec[3] - rec[1]) * (rec[2] - rec[0])
            #当前rec的四个顶点
            for c in [(rec[0], rec[1]), (rec[2], rec[3]), (rec[0], rec[3]), (rec[2], rec[1])]:
                if c in corner:
                    corner.remove(c)
                else:
                    corner.add(c)
        #若范围总和不等于最终4个点内的范围和
        if sums != (R - L) * (D - U):
            return False
        #四个最终边界点
        bigCorner = [(L, U), (L, D), (R, U), (R, D)]
        for bc in bigCorner:
            if not bc in corner:
                return False
            corner.remove(bc)
        #其它顶点是否只出现2次或者4次
        return True if not corner else False


rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
solute = Solution()
res = solute.isRectangleCover(rectangles)
        


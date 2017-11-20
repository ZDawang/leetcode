#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-5-17
#difficulty degree：
#problem: 42_trapping_rain_water
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #每个点的存水量取决于左右两边的最大高度
    def trap(self, height):
        l = len(height)
        #存储每个点的左右两边的最高高度
        d_pos, d_opp = {}, {}
        h_pos, h_opp = 0, 0
        for i in range(l):
            h_pos = max(h_pos, height[i])
            h_opp = max(h_opp, height[l - 1 - i])
            d_pos[i] = h_pos
            d_opp[l - 1 - i] = h_opp

        res = 0
        for i in range(l):
            h = min(d_opp[i], d_pos[i]) - height[i]
            res += h
        return res



height = [5,2,1,2,1,5]
solute = Solution()
res = solute.trap(height)
print(res)
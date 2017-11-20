#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 506_Relative_Ranks.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #排序，对(num,index)进行排序
    def findRelativeRanks(self, nums):
        numIndex = [(num, index) for index, num in enumerate(nums)]
        numIndex.sort(reverse = True)
        res = [0] * len(nums)
        for i, (num, index) in enumerate(numIndex):
            if i == 0:
                res[index] = "Gold Medal"
            elif i == 1:
                res[index] = "Silver Medal"
            elif i == 2:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(i + 1)
        return res
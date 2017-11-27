#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 491_Increasing_Subsequences.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS
    #使用set来存储结果，避免重复。因为set不能存储可变的list，所以使用tuple
    #最后再转成list
    def findSubsequences(self, nums):
        #tmp是当前的中间结果。i为nums的下标
        def dfs(tmp, i):
            if len(tmp) >= 2: 
                res.add(tmp)
            if i >= len(nums): 
                return
            #不加入新的下标对应的数
            dfs(tmp, i + 1)
            #当前下标对应的数比tmp的最后一位大时
            if not tmp or tmp[-1] <= nums[i]:
                dfs(tmp + (nums[i], ), i + 1)

        res = set()
        dfs((), 0)
        return [list(tmp) for tmp in res]

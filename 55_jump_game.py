#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 55_jump_game
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE  :  DFS
    def canJump2(self, nums):
        def recurse(start, nums, l, res):
            if True in res:
                return
            if start == l:
                res.append(True)
            if start > l:
                return False
            if nums[start] == 0:
                return False
            for i in range(1, nums[start] + 1):
                recurse(start + i, nums, l, res)
        start = 0
        l = len(nums) - 1
        res = []
        recurse(0, nums, l, res)
        if True in res:
            return True
        return False


    def canJump(self, nums):
        k = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                k += 1
            else:
                if k:
                    if nums[i] <= k:
                        k += 1
                    else:
                        k = 0
        return False if k else True

    #贪心算法,计算每一步的最小距离与最大距离
    def canJump(self, nums):
        l, r = 0, 0
        while l <= r and r < len(nums) - 1:
            prer = r
            for i in range(l, prer + 1):
                r = max(i + nums[i], r)
            l = prer + 1
        return r >= len(nums) - 1


nums = [3,2,1,0,4]
solute = Solution()
res = solute.canJump(nums)

print(res)
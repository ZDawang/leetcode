#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-13
#difficulty degree：
#problem: 16_3Sum_closest
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思路，将3sum变为2sum。
    def threeSumClosest(self, nums, target):
        nums.sort()
        len_nums = len(nums)
        if len_nums < 3:
            return 0
        res = sum(nums[:3])
        dis = abs(sum(nums[:3]) - target)
        for i in range(len_nums-2):
            if nums[i] > target//3:
                return res
            l, r = i+1, len_nums - 1
            while(l < r):
                temp = nums[i] + nums[l] + nums[r]
                if temp-target == 0:
                    return temp
                if abs(temp - target) < dis:
                    res = nums[i] + nums[l] + nums[r]
                    dis = abs(temp - target)
                l, r = (l+1, r) if temp-target<0 else (l, r-1)
        return res

    #将3sum变为2sum。
    #对nums进行排序。从第一个数字向后进行遍历，固定3个数的第一个为此数字。
    #对剩下两个数字寻找target-num的最近的组合。计算差值。
    def threeSumClosest2(self, nums, target):
        #双指针，进行2sumClosest的寻找。
        def twoSumClosest(nums, start, target):
            if start >= len(nums) - 1:
                return float("inf")
            l, r = start, len(nums) - 1
            res = nums[l] + nums[r]
            while l < r:
                #更新l或r
                tmp = nums[l] + nums[r]
                if tmp < target:
                    l += 1
                else:
                    r -= 1
                #更新res
                if abs(res - target) > abs(tmp - target):
                    res = tmp
            return res

        if len(nums) < 3: return 0
        res = float("inf")
        nums.sort()
        for i, num in enumerate(nums):
            tmp = num + twoSumClosest(nums, i + 1, target - num)
            if abs(res - target) > abs(tmp - target):
                res = tmp
        return res





nums = [1,1,1,0]

solute = Solution()
res = solute.threeSumClosest2(nums, 82)
print(res)
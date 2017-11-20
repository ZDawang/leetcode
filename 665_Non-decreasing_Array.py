#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 665_Non-decreasing_Array.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #如果nums[i] < nums[i - 1],那么需要调整nums[i]，nums[i-1]中的一个
    #若增大nums[i],则对后面不利
    #若减小nums[i-1],则对前面不一定可以成立
    #所以先判断是否可以通过减小nums[i-1]，若不可以，再调整nums[i]
    #isModify用来判断是否已经更改过
    def checkPossibility(self, nums):
        l = len(nums)
        if l <= 2: return True
        isModify = False
        for i in range(1, l):
            if nums[i] < nums[i - 1]:
                if isModify: return False
                #调整nums[i - 1]
                if i == 1 or nums[i] >= nums[i - 2]:
                    isModify = True
                #调整nums[i]
                else:
                    nums[i] = nums[i - 1]
                    isModify = True
        return True

                    


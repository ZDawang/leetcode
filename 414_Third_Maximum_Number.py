#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 414_Third_Maximum_Number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #先找到最小数，然后设置3个数为最大数进行更新。
    def thirdMax(self, nums):
        minNum = min(nums)
        maxNums = [minNum, minNum, minNum]
        for num in nums:
            if num <= maxNums[2]:
                continue
            elif num > maxNums[2] and num < maxNums[1]:
                maxNums[2] = num
            elif num > maxNums[1] and num < maxNums[0]:
                maxNums[1], maxNums[2] = num, maxNums[1]
            elif num > maxNums[0]:
                maxNums = [num] + maxNums[:2]

        if maxNums[0] != maxNums[1] and maxNums[1] != maxNums[2]:
            return maxNums[2]
        return maxNums[0]

nums = [1, 2]
solute = Solution()
res = solute.thirdMax(nums)
print(res)
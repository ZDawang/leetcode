#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-4
#difficulty degree：
#problem: 376_Wiggle_Subsequence
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(n2)思路，跟最长上升子序列一样，dp存储到当前的最大子序列中数字个数，不过加一个符号位
    #以结果作为dp
    def wiggleMaxLength(self, nums):
        if not nums: return 0
        l = len(nums)
        dp = [1] * l

        for i in range(1, l):
            temp = 1
            sign = 1
            for j in range(i):
                absdp = abs(dp2[j])
                if (nums[i] - nums[j])*dp[j] > 0:
                    if absdp + 1 > temp:
                        temp = absdp + 1
                        sign = -dp[j]//absdp
            dp[i] = sign * temp

        dp2 = [-1] * l
        for i in range(1, l):
            temp = 1
            sign = 1
            for j in range(i):
                absdp = abs(dp2[j])
                if (nums[i] - nums[j])*dp2[j] > 0:
                    if absdp + 1 > temp:
                        temp = absdp + 1
                        sign = -dp2[j]//absdp
            dp2[i] = sign * temp
        return max(abs(dp[-1]), abs(dp2[-1]))

    #O(n)
    #up表示到当前数字，最后数字为上升的最长子序列的长度。
    #down表示到当前数字，最后数字为下降的最长子序列的长度。
    def wiggleMaxLength(self, nums):
        if not nums: return 0
        l = len(nums)
        up, down = [1] * l, [1] * l
        for i in range(1, l):
            #若当前数字比前一个数字大，则up[i] = down[i-1] + 1
            up[i] = down[i - 1] + 1 if(nums[i] > nums[i - 1]) else up[i - 1]
            #若当前数字比前一个数字小，则down[i] = up[i-1] + 1
            down[i] = up[i - 1] + 1 if(nums[i] < nums[i - 1]) else down[i - 1]
        return max(up[-1], down[-1])

    #优化空间复杂度
    def wiggleMaxLength(self, nums):
        if not nums: return 0
        l = len(nums)
        up, down = 1, 1
        for i in range(1, l):
            preup = up
            up = down + 1 if(nums[i] > nums[i - 1]) else up
            down = preup + 1 if(nums[i] < nums[i - 1]) else down
        return max(up, down)


nums = [1,17,5,10,13,15,10,5,16,8]
solute = Solution()
res = solute.wiggleMaxLength(nums)
print(res)
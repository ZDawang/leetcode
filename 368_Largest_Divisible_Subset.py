#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 368_Largest_Divisible_Subset.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP
    #先对nums进行sort，使数字从小到大排列。
    #使用temp来存储每个num与它前面的数字能组成的最大subset的长度。
    #使用d存储当前num所在的subset的前面一个数字。
    def largestDivisibleSubset(self, nums):
        if not nums: return []
        nums.sort()
        temp, d = [1], {}
        max_res, index_res = 0, 0
        for i in range(1, len(nums)):
            max_l = 1
            for j in range(i):
                #找到当前数字与前面数字组成的最大subset
                if nums[i] % nums[j] == 0:
                    if (temp[j] + 1) > max_l:
                        max_l = temp[j] + 1
                        d[i] = j
            temp.append(max_l)
            if max_l > max_res:
                max_res = max_l
                index_res = i
        res = []
        while(index_res in d):
            res.append(nums[index_res])
            index_res = d[index_res]
        res.append(nums[index_res])
        return res


    #DP，时间复杂度O(n2)
    #因为排序之后，则每个数据只要能够整除前面set中的最大数字，则可以加入到这个set中。
    #对每个数字，存储它与前面数字组成的最大set长度，时间复杂度O(n2)以及set中前面一个数字。
    def largestDivisibleSubset(self, nums):
        if not nums: return []
        nums.sort()
        l = len(nums)
        dp, set_len = [i for i in range(l)], [1] * l
        #对每个数字，都找到它所在的最大set长度以及前一个数字
        for i in range(l):
            for j in range(i):
                if nums[i] % nums[j] != 0:
                    continue
                if set_len[j] + 1 > set_len[i]:
                    set_len[i], dp[i] = set_len[j] + 1, j
        #回溯找到最大set里的所有数字，时间复杂度O(n2)
        res = []
        i = set_len.index(max(set_len))
        while dp[i] != i:
            res.append(nums[i])
            i = dp[i]
        res.append(nums[i])
        return res





solute = Solution()
nums = [3,4,8,16]
res = solute.largestDivisibleSubset(nums)
print(res)

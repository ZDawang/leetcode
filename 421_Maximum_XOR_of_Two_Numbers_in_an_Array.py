#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 421_Maximum_XOR_of_Two_Numbers_in_an_Array.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):

    def findMaximumXOR(self, nums):
        res, mask = 0, 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            s = set()
            for num in nums:
                s.add(num & mask)
            #将res在i位的0变为1，变为候选的res
            tmp = res | (1 << i)
            #查找是否有两个数nums[i], nums[j]，这两个数的前32-i位相异或等于候选的res
            #因为nums[i] ^ nums[j] = tmp, 所以 tmp ^ nums[i] = nums[j]
            #所以查找tmp^nums[i]是否存在于s中，就可以知道有没有与nums[i]对应的nums[j]
            for prefix in s:
                #若有，则可以更新最大值
                if tmp ^ prefix in s:
                    res = tmp
                    break
        return res



nums = [3,10,5,25,2,8]
solute = Solution()
res = solute.findMaximumXOR(nums)

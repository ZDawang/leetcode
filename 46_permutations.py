#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-31
#difficulty degree：
#problem: 46_permutations
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def permute(self, nums):
        def recurse(d, res, l):
            if -1 in d.values():
                return
            if sum(d.values()) == 0:
                res.append(l)
                return
            for d_element in d:
                temp = d.copy()
                temp[d_element] -= 1
                recurse(temp, res, l + [d_element])
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        res = []
        recurse(d, res, [])
        return res

nums = [1,1,2]
solute = Solution()
res = solute.permute(nums)

print(res)

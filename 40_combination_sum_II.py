#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-27
#difficulty degree：
#problem: 40_combination_sum_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def combinationSum2(self, candidates, target):
        #借用前面寻找N个数之和为target，将N取值变化
        def search(nums, target, k, res_num, res):
            if len(nums) < k or k < 2 or target < nums[0]*k or target > nums[-1] * k:
                return
            if k == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        res.append(res_num + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        if nums[l] + nums[r] < target:
                            l += 1
                        else:
                            r -= 1
            else:
                for i in range(len(nums) - k + 1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        search(nums[i + 1:], target - nums[i], k  - 1, res_num + [nums[i]], res)
            return res

        candidates.sort()
        l = len(candidates)
        res = []
        if target in candidates:
            res.append([target])

        print(max(2, target //  candidates[-1]), min(target // candidates[0] + 1, l))
        for i in range(min(2, target //  candidates[-1] + 1), target // candidates[0] + 1):
            search(candidates, target, i, [], res)
        return res

candidates = [10, 1, 2, 7, 6, 1, 5]

solute = Solution()

res = solute.combinationSum2(candidates, 8)

print(res)
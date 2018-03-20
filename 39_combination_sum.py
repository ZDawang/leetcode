#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-27
#difficulty degree：
#problem: 39_combination_sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def combinationSum(self, candidates, target):
        #借用前面寻找N个数之和为target，将N取值变化
        def search(nums, target, k, res_num, res):
            if k < 2 or target < nums[0]*k or target > nums[-1] * k:
                return
            if k == 2:
                l, r = 0, len(nums) - 1
                while l <= r:
                    if nums[l] + nums[r] == target:
                        res.append(res_num + [nums[l], nums[r]])
                        l += 1
                        while l <r and nums[l] == nums[l + 1]:
                            l += 1
                    else:
                        if nums[l] + nums[r] < target:
                            l += 1
                        else:
                            r -= 1
            else:
                for i in range(len(nums)):
                        search(nums[i:], target - nums[i], k  - 1, res_num + [nums[i]], res)
            return res

        candidates.sort()
        l = len(candidates)
        if l == 1:
            if target % candidates[0] == 0:
                return [(target // candidates[0])*[candidates[0]]]
        res = []
        if target in candidates:
            res.append([target])

        print(max(2, target //  candidates[-1]), target // candidates[0] + 1)
        for i in range(min(2, target //  candidates[-1] + 1), target // candidates[0] + 1):
            search(candidates, target, i, [], res)
        return res


    #DFS+剪枝
    def combinationSum2(self, candidates, target):
        def dfs(i, sums, tmp):
            if sums == target:
                res.append(tmp[:])
                return
            if sums > target:
                return
            for j in range(i, len(candidates)):
                tmp.append(candidates[j])
                dfs(j, sums + candidates[j], tmp)
                tmp.pop()

        if not candidates: return []
        candidates.sort()
        res = []
        for i in range(len(candidates)):
            dfs(i, candidates[i], [candidates[i]])
        return res







candidates = [1,2]

solute = Solution()

res = solute.combinationSum(candidates, 4)

print(res)
#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-14
#difficulty degree：
#problem: 18_4sum
#time_complecity:  
#space_complecity: 
#beats: 

#将4个数的累加变成，固定两个数，然后two sum
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()

        d={}
        res = []
        len_nums = len(nums)
        
        if len_nums < 4:
            return res
        for i in range(len_nums):
            d[nums[i]] = i
        for i in range(len_nums-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if 4*nums[i] > target:
                return res
            p1 = i+1
            while (3*nums[p1] <= target - nums[i]) and p1 < len_nums - 2:
                p2 = p1+1
                while (2*nums[p2] <= target - nums[i] - nums[p1]) and p2 < len_nums - 1:
                    if target-nums[i]-nums[p1]-nums[p2] in d:
                        if d[target-nums[i]-nums[p1]-nums[p2]] > p2:
                            res.append([nums[i], nums[p1], nums[p2], target-nums[i]-nums[p1]-nums[p2]])
                    while nums[p2] == nums[p2+1] and p2<len_nums -2:
                        p2 = p2 + 1
                    p2 = p2 + 1
                while nums[p1] == nums[p1 + 1] and p1<len_nums-2:
                    p1 = p1 +1
                p1 = p1 + 1
        return res




class Solution2(object):
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return
            if N == 2:
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        results = []
        findNsum(sorted(nums), target, 3, [], results)
        return results

    #答案区的一个非常好的方法，用递归实现任意数量数字的和，而且通过排序后剪枝，可以使时间非常快。
    #时间复杂度为O(N**3)
    def fourSum2(self, nums, target):
        #start用来标明在nums的位置，target为剩下的数值，k为剩下的数字个数
        def helper(nums, start, target, k, tmp, res):
            #当target太小或太大，或者剩下数字不够k个时
            if (k > len(nums) - start) or (target > nums[-1] * k) or target < (nums[start] * k):
                return
            if k > 2:
                for i in range(start, len(nums)):
                    #避免重复将同一个数字加到同一个位置。
                    if (i == start) or (nums[i] != nums[i - 1]):
                        tmp.append(nums[i])
                        helper(nums, i + 1, target-nums[i], k-1, tmp, res)
                        tmp.pop()
            elif k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(tmp + [nums[l], nums[r]])
                        l += 1
                        #避免重复把同一对数字重复加到结果中。
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            return

        res = []
        nums.sort()
        helper(nums, 0, target, 4, [], res)
        return res



nums = [-1,2,2,-5,0,-1,4]
target = 3

solute = Solution2()
res = solute.fourSum2(nums, target)

print(res)
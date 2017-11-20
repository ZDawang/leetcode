#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 659_Split_Array_into_Consecutive_Subsequences.py
#time_complecity:  
#space_complecity: 
#beats: 
import collections
class Solution(object):
    def isPossible(self, nums):
        l = len(nums)
        pre, p1, p2, p3 = float("-inf"), 0, 0, 0
        cur, cnt, c1, c2, c3 = 0, 0, 0, 0, 0
        i = 0
        while i < l:
            cur, cnt = nums[i], 0
            while i < l and cur == nums[i]:
                cnt += 1
                i += 1
            if cur != pre + 1:
                if p1 != 0 or p2 != 0:
                    return False
                c1, c2, c3 = cnt, 0, 0
            else:
                if cnt < p1 + p2: return False
                if cnt > p1 + p2 + p3:
                    c1 = cnt - (p1 + p2 + p3)
                    c2 = p1
                    c3 = p2 + p3
                else:
                    c1 = 0
                    c2 = p1
                    c3 = p2 + cnt - (p1 + p2)
            pre, p1, p2, p3 = cur, c1, c2, c3
        return p1 == 0 and p2 == 0



nums = [1,2,3,3,4,5]
solute = Solution()
res = solute.isPossible(nums)




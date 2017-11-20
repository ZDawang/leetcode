#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-7
#difficulty degree：
#problem: 77_combinations
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def combine(self, n, k):
        def recurse(n, k, min_num, list_temp, res):
            if len(list_temp) == k:
                res.append(list_temp)
                return
            for i in range(min_num, n + 1):
                if i not in list_temp:
                    recurse(n, k, i + 1, list_temp + [i], res)

        res = []
        recurse(n, k, 1, [], res)
        return res

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
        



solute = Solution()
res = solute.combine(9, 2)
print(res)
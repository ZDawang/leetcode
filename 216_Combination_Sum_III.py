#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 216_Combination_Sum_III
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用栈，来控制，从前往后，从小到大, x为要放置的下一个数
    def combinationSum3(self, k, n):
        stack = []
        res = []
        x = 1
        while 1:
            l = len(stack)
            if l == k and sum(stack) == n:
                res.append(stack[:])
            if x > 9 or l == k:
                if not stack:
                    return res
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
            print(stack, x)

solute = Solution()
res = solute.combinationSum3(3, 9)
print(res)
#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 402_Remove_K_Digits.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #若是最小的，则尽量把前面大的数消掉
    #比如4321，首先应该把4消掉。
    #使用栈来存储当前消除后的结果，进行下一步的消除操作。
    def removeKdigits(self, num, k):
        stack = []
        for n in num:
            while stack and k > 0 and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        return "".join(stack[:len(stack) - k]).lstrip("0") or "0"

num = "112"
k = 1
solute = Solution()
res = solute.removeKdigits(num, k)
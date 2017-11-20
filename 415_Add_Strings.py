#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 415_Add_Strings
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def addStrings(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        l = max(l1, l2)
        if l1 > l2:
            num2 = "0" * (l1 - l2) + num2
        else:
            num1 = "0" * (l2 - l1) + num1
        carry = 0
        res = ""
        for i in range(l):
            res = str((int(num1[l - 1- i]) + int(num2[l - 1- i]) + carry) % 10) + res
            carry = (int(num1[l - 1- i]) + int(num2[l - 1- i]) + carry) // 10
        return res if carry == 0 else "1" + res

solute = Solution()
res = solute.addStrings("9", "99")
print(res)
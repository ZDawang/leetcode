#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 202_Happy_Number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def splitnum(self, num):
        if num <= 9:
            return [num]
        numlist = []
        while(num > 9):
            numlist.append(num % 10)
            num = num // 10
        return numlist + [num]


    def isHappy(self, n):
        d_sqr = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
        res = {}
        sumnum = n
        while res.get(sumnum, 0) != 2:
            numlist = self.splitnum(sumnum)
            sumnum = 0
            for n in numlist:
                sumnum += d_sqr[n]
            if sumnum == 1:
                return True
            res[sumnum] = res.setdefault(sumnum, 0) + 1
        return False

n = 3
solute = Solution()
res = solute.isHappy(n)
print(res)
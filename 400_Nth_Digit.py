#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 400_Nth_Digit
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #寻找n在哪个范围，i为十进制数的位数。找到后再找到对应的数
    def findNthDigit(self, n):
        i, j = 1, 9
        while(n > 9):
            j *= 10
            i += 1
            n -= i*j
        n += i*j - 10
        return int(str(10**(i - 1) + n//i)[n%i])

solute = Solution()
res = solute.findNthDigit(9)
print(res)

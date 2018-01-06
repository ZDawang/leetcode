#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 728_Self_Dividing_Numbers.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #检查每个数是否满足，然后将满足的数加入结果
    def selfDividingNumbers(self, left, right):
        #判断当前数字是否满足条件。
        def isDivding(num):
            tmp = num
            while tmp != 0:
                tmp, remain = tmp//10, tmp%10
                if remain == 0 or num%remain != 0:
                    return False
            return True

        return [num for num in range(left, right + 1) if isDivding(num)]

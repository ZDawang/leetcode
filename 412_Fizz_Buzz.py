#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def fizzBuzz(self, n):
        res = [""] * (n + 1)
        for i in range(1, n + 1):
            tmp = "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)
            res[i] = tmp or str(i)
        res.pop(0)
        return res

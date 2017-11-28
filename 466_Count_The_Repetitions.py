#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 466_Count_The_Repetitions.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #cycle,寻找多少个s1可以构成整数个s2
    #如果两个s1对应的s2的起始位置相同，则可以认为这两个s1之间构成一个循环
    #s1可以分为三部分。第一部分是循环开始前的部分，第二部分是循环部分，第三部分是循环后部分。
    #第二部分可以直接算出，第一部分与第三部分可以连在一起，看成一个循环部分的前面一部分。
    def getMaxRepetitions(self, s1, n1, s2, n2):
        #寻找下一个s2的开始位置以及重复次数
        def findNextStart(s1, s2, index2):
            l2, r2 = len(s2), 0
            for c in s1:
                if c == s2[index2]:
                    index2 += 1
                    if index2 == l2:
                        r2, index2 = r2 + 1, 0
            return index2, r2
        #如果s2的字母s1中没有的话，则返回0
        for c in s2:
            if s1.find(c) < 0: return 0

        start = {}
        r1, r2, index2 = 0, 0, 0
        while r1 < n1:
            index2, tmp = findNextStart(s1, s2, index2)
            r1, r2 = r1 + 1, r2 + tmp
            #找到cycle
            if index2 in start:
                prer1, prer2 = start[index2]
                #一个cycle。s1，s2的循环次数
                repeat1, repeat2 = r1 - prer1, r2 - prer2
                #剩下的n1，从0到prer1，以及循环剩下的一小段
                leftn1 = (n1 - prer1)%repeat1 + prer1
                res = (n1 - prer1)//repeat1 * repeat2
                #因为剩下的s1也是从0开始的，所以直接查字典。
                for r1, r2 in start.values():
                    if r1 == leftn1:
                        return (res + r2)//n2
            start[index2] = (r1, r2)
        return r2//n2










#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 686_Repeated_String_Match.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #对于每个A的元素开头，都测试一遍。
    #TLE
    def repeatedStringMatch(self, A, B):
        la, lb, j = len(A), len(B), 0
        times = 1
        for i in range(la):
            if A[i] == B[j]:
                while j != lb and A[i] == B[j]:
                    i = (i + 1) % la
                    times += i == 0
                    j += 1
                if j == lb: return times if i != 0 else times - 1
                j, times = 0, 1
        return -1

    #在newA里寻找
    def repeatedStringMatch3(self, A, B):
        la, lb = len(A), len(B)
        newA = A * (lb //la + 2)
        pos = newA.find(B)
        return (pos+lb)//la+ ((pos+lb)%la != 0) if pos != -1 else -1

    #使用KMP算法进行改进
    #i为A的指针，j为B的指针
    #本质还是字符串匹配问题。所以只需要把A看成无限长的字符串，找到最早匹配到B的位置即可。
    #若可以匹配到，则i肯定满足：i <= la + lb，使用这个条件来判断是否可以匹配
    #若已经匹配到，则可根据i的值来计算循环的次数。
    def repeatedStringMatch2(self, A, B):
        la, lb = len(A), len(B)
        tableB = self.getNext(B)
        i, j = 0, 0
        #防止出现无法匹配到的情况
        while i <= la + lb:
            #若寻找到了B的末尾，即匹配成功，根据i计算循环的次数
            if j == lb:
                return (i//la) + (i%la != 0)
            if A[i%la] == B[j]:
                i, j = i + 1, j + 1
            else:
                j = tableB[j] - 1
                if j == -1:
                    i, j = i + 1, j + 1
        return -1

    #构建跳转表
    def getNext(self, S):
        table = [0] * len(S)
        for i in range(1, len(S)):
            index = table[i - 1]
            while index > 0 and S[index] != S[i]:
                index = table[index - 1]
            table[i] = index + 1 if S[index] == S[i] else 0
        return table




A = "a"
B = "aa"
solute = Solution()
res = solute.repeatedStringMatch2(A, B)
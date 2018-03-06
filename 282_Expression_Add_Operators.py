#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 282_Expression_Add_Operators.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS, 需要小心的地方是数字不能为0开头的。所以分治一下。
    def addOperators(self, num, target):
        #由于乘法的优先性，tmp存储已经累加的结果，prenum为正在乘法中的结果
        def dfs(num, sumtmp, prenum, target, tmp):
            if not num:
                if sumtmp + prenum == target:
                    res.append(tmp)
                return
            if num[0] == "0":
                #加法
                dfs(num[1:], sumtmp + prenum, 0, target, tmp + "+" + "0")
                #减法
                dfs(num[1:], sumtmp + prenum, 0, target, tmp + "-" + "0")
                #乘法
                dfs(num[1:], sumtmp, 0, target, tmp + "*" + "0")
            else:    
                for i in range(1, len(num) + 1):
                    #加法
                    dfs(num[i:], sumtmp + prenum, int(num[:i]), target, tmp + "+" + num[:i])
                    #减法
                    dfs(num[i:], sumtmp + prenum, -int(num[:i]), target, tmp + "-" + num[:i])
                    #乘法
                    dfs(num[i:], sumtmp, prenum * int(num[:i]), target, tmp + "*" + num[:i])

        if not num: return []
        res = []
        if num[0] == "0":
            dfs(num[1:], 0, 0, target, num[:1])
        else:
            for i in range(1, len(num) + 1):
                dfs(num[i:], 0, int(num[:i]), target, num[:i])
        return res



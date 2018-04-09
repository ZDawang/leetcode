#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 306_Additive_Number.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
        def dfs(pre, cur, j):
            if dfs.res:
                return
            if j >= len(num):
                dfs.res = True
                return
            sums = str(pre + cur)
            if num[j: j+len(sums)] != sums:
                return
            dfs(cur, int(sums), j+len(sums))

        dfs.res = False
        #对前两个数进行遍历
        if len(num) < 3:
            return False
        for i in range(1, len(num)-1):
            if i != 1 and num[0] == "0":
                continue
            for j in range(i + 1, len(num)):
                if i + 1 != j and num[i] == "0":
                    break
                dfs(int(num[:i]), int(num[i: j]), j)
        return dfs.res
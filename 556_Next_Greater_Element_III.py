#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-27
#difficulty degree：
#problem: 556_Next_Greater_Element_III
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def nextGreaterElement(self, n):
        nlist = [int(c) for c in str(n)]
        l = len(nlist)
        for i in range(l - 2, -1, -1):
            #不是降序
            if nlist[i] < nlist[i + 1]:
                #寻找比当前值大的最小数
                num = 9
                index = 0
                for j in range(i + 1, l):
                    if nlist[j] > nlist[i]:
                        num = min(num, nlist[j])
                        index = j
                nlist[index], nlist[i] = nlist[i], num
                nlist = nlist[: i + 1] + sorted(nlist[i + 1:])
                res = int("".join([str(c) for c in nlist]))
                return res if res <= 2**31 - 1 else -1
        return -1

n = 1999999999
solute = Solution()
res = solute.nextGreaterElement(n)

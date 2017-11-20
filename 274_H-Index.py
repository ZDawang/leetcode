#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-18
#difficulty degree：
#problem: 274_H-Index
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #目的：寻找大于等于n，数量也大于等于n的n值
    #方法：首先统计每个值出现的次数，然后找累计值大于下标的最大值
    def hIndex(self, citations):
        l = len(citations)
        cnt = [0 for i in range(l + 1)]
        for c in citations:
            cnt[min(c, l)] += 1
        total = 0
        for i in range(l, -1, -1):
            total += cnt[i]
            if total >= i:
                return i
        return 0


citations = [1, 1]
solute = Solution()
res = solute.hIndex(citations)
print(res)


#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 763_Partition_Labels
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #贪心算法。当一个窗口中的字母全部出现时，则切分。
    def partitionLabels(self, S):
            def isSame(d, counts):
            for c in d:
                if d[c] < counts[c]:
                    return False
            return True
        
        counts = Counter(S)
        start, d = -1, {}
        res = []
        for i in range(len(S)):
            d[S[i]] = d.get(S[i], 0) + 1
            if isSame(d, counts):
                res.append(i - start)
                start, d = i, {}
        return res
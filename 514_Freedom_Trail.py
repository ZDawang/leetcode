#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-20
#difficulty degree：
#problem: 514_Freedom_Trail
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findRotateSteps(self, ring, key):
        lr = len(ring)
        lk = len(key)
        dp = [10000] * lr
        #获得ring中各个字母的位置
        d = {}
        for i in range(lr):
            if ring[i] in d:
                d[ring[i]].append(i)
            else:
                d[ring[i]] = [i]
        #获得第一步的dp，供后面迭代
        for loc in d[key[0]]:
            dp[loc] = min(abs(loc), lr - abs(loc))
        #迭代，寻找下一个字母
        for i in range(1, lk):
            newdp = [10000] * lr
            for j in range(lr):
                if dp[j] == 10000:
                    continue
                else:
                    for loc in d[key[i]]:
                        step = min(abs(loc - j), lr - abs(loc - j))
                        newdp[loc] = min(newdp[loc], dp[j] + step)
            dp = newdp
        return min(dp) + lk


ring = "godding"
key = "gdg"
solute = Solution()
res = solute.findRotateSteps(ring, key)
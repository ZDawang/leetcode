#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 134_Gas_Station.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #意思是，从哪个站出发，还要回到哪个站
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        remain = 0
        start = 0
        for i, g in enumerate(gas):
            #扣除到这个站使用的油量
            remain -= cost[i - 1]
            #如果到不了这个站
            if remain < 0:
                remain, start = 0, i
            #加油
            remain += g
        return start

    #可以改造成如果油箱不是无限的情况
    def canCompleteCircuit2(self, gas, cost):
        if not cost: return -1
        remain, start = 0, 0
        gasNeedForStationZero = 0
        for i, g in enumerate(gas):
            #扣除到这个站使用的油量
            remain -= cost[i - 1]
            #如果到不了这个站
            if remain < 0:
                gasNeedForStationZero -= remain
                remain, start = 0, i
            #加油
            remain += g
        #看是否能回的到0，并且足够支撑0后面的路途
        return start if remain >= gasNeedForStationZero else -1


gas = [2, 4]
cost = [3, 4]
solute = Solution()
res = solute.canCompleteCircuit(gas, cost)
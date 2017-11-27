#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #每次禁止下面离他最近的
    #banR代表下面可以禁止的R有多少个
    #aliveR代表总共剩下多少个R议员
    def predictPartyVictory(self, senate):
        banR, banD = 0, 0
        aliveR, aliveD = senate.count("R"), senate.count("D")
        alive = [True] * len(senate)
        #当都有议员剩下时
        while aliveR > 0 and aliveD > 0:
            for i, s in enumerate(senate):
                if not alive[i]: continue
                if s == "R":
                    if banR != 0:
                        banR -= 1
                        alive[i] = False
                    else:
                        banD += 1
                        aliveD -= 1
                else:
                    if banD != 0:
                        banD -= 1
                        alive[i] = False
                    else:
                        banR += 1
                        aliveR -= 1
        return "Radiant" if aliveR > aliveD else "Dire"

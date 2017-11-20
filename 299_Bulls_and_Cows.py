#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-19
#difficulty degree：
#problem: 299_Bulls_and_Cows
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def getHint(self, secret, guess):
        s_str = str(secret)
        g_str = str(guess)
        sd, gd = {}, {}
        bull = 0
        for i in range(len(s_str)):
            if s_str[i] == g_str[i]:
                bull += 1
                continue
            sd[s_str[i]] = sd.get(s_str[i], 0) + 1
            gd[g_str[i]] = gd.get(g_str[i], 0) + 1
        cow = 0
        for s in sd:
            cow += min(gd.get(s, 0), sd[s])
        return str(bull) + 'A' + str(cow) + 'B'

secret = 1807
guess = 7810
solute = Solution()
res = solute.getHint(secret, guess)
print(res)

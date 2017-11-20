#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-13
#difficulty degree：
#problem: 91_decode_ways
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def numDecodings(self, s):
        def dfs(s, res):
            if len(s) <= 1 :
                if len(s) == 0:
                    res[0] += 1
                    return
                else:
                    if s[0] != '0':
                        res[0] += 1
                        return
            if s[0] != '0':
                dfs(s[1:], res)
            if int(s[0:2]) <= 26 and s[0] != '0':
                dfs(s[2:], res)
        res = [0]
        dfs(s, res)
        return res[0] if s else 0


    def numDecodings2(self, s):
        #当数与前面的一个数小于26时，结果等于前两个结果之和
        if not s or s[0] == '0':
            return 0
        res, res_delay = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    res, res_delay = res_delay, res
                else:
                    res, res_delay = 0, 0
            else:
                if s[i - 1] == '0':
                    res, res_delay = res, res
                else:
                    if int(s[i - 1] + s[i]) <= 26:
                        res, res_delay = res + res_delay, res
                        print(i, res, res_delay)
                    else:
                        res, res_delay = res, res   
        return res
            


s = "1111101111"
solute = Solution()
res = solute.numDecodings(s)
print(res)
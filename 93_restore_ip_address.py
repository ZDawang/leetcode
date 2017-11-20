#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-14
#difficulty degree：
#problem: 93_restore_ip_address
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def restoreIpAddresses(self, s):
        def dfs(s, st, l, res):
            if l == 3:
                print(st, s)
                if not s:
                    return
                if int(s) <= 255 and (len(s) == 1 or (len(s) > 1 and s[0] != '0')):
                    res.append(st + '.' + s)
                return
            for i in range(1, min(len(s), 3) + 1):
                if int(s[:i]) <= 255 and (i == 1 or (i > 1 and s[0] != '0')):
                        dfs(s[i:], st + '.' + s[:i], l + 1, res)
        res = []
        dfs(s, "", 0, res)
        res = [r[1:] for r in res]
        return res

s = "255255255255"
solute = Solution()
res = solute.restoreIpAddresses(s)
print(res)
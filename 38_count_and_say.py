#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-25
#difficulty degree：
#problem: 38_count_and_say
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def countAndSay(self, n):
        # 产生一个数的下一个数
        def count_recurse(n_str):
            count = 1
            res = ""
            l = len(n_str)
            for i in range(l - 1):
                if n_str[i] == n_str[i + 1]:
                    count += 1
                else:
                    res = res + str(count) + n_str[i]
                    count = 1
            res = res + str(count) + n_str[-1]
            return res

        res = '1'
        for i in range(n-1):
            res = count_recurse(res)
        return res


n = 5

solute = Solution()

res = solute.countAndSay(n)

print(res)
#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 60_permutation_sequence
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #LTE
    def getPermutation(self, n, k):
        def generate(n, string, res):
            if len(string) == n:
                res.append(string)
                return
            for i in range(1, n + 1):
                if str(i) not in string:
                    generate(n, string + str(i), res)

        res = []
        generate(n, "", res)
        #print(res)
        #print(res[k-1])
        return res[k - 1]

    def getPermutation2(self, n, k):
        #通过k直接算出每一位的数
        def recurse(factorial, res, stack, k, div):
            if k % factorial == 0:
                res.append(stack[k//factorial-1])
                stack.pop(k//factorial-1)
                for i in range(len(stack) - 1, -1, -1):
                    res.append(stack[i])
                return
            index = k // factorial
            k = k % factorial
            factorial = factorial // div
            div -= 1
            res.append(stack[index])
            stack.pop(index)
            recurse(factorial, res, stack, k, div)

        #计算阶乘
        factorial = 1
        for i in range(1, n):
            factorial *= i
        stack = [i for i in range(1, n + 1)]
        res = []
        recurse(factorial, res, stack, k, n - 1)
        res_str = ""
        for r in res:
            res_str += str(r)
        return res_str

        


solute = Solution()
for i in range(1, 25):
    res = solute.getPermutation2(4, i)
    print(res)
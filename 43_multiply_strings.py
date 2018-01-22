#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 43_multiply_strings
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def multiply(self, num1, num2):
        if num1 == '0' or num2 =='0':
            return "0"
        res = [0] * (len(num1) + len(num2))
        index = len(num1) + len(num2)
        for n1 in reversed(num1):
            index = index - 1
            start = index
            for n2 in reversed(num2):
                res[start] += int(n1) * int(n2)
                res[start - 1] += res[start] // 10
                res[start] %= 10
                start -= 1
        return ''.join(map(str,res[0:])) if res[0] != 0 else ''.join(map(str,res[1:]))


    #按照小学摆算式的方法运算
    #index为所需要放的位置。res[0]为最低位，res[-1]为最高位.
    def multiply2(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            index = i
            for n2 in reversed(num2):
                tmp = int(n1) * int(n2)
                start, remain = index, 0
                #一直向前运算，直到进位为0
                while tmp > 0:
                    tmp, res[start] = divmod(res[start] + tmp, 10)
                    start += 1
                index += 1
        #因为乘法，最高位可能用不到，比如30*30=900，结果只用到了3位。
        if res[-1] == 0: res.pop()
        return "".join(map(str, res[::-1]))






num1 = "300"
num2 = "30"

solute = Solution()
res = solute.multiply2(num1, num2)

#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 67_add_binary
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #先计算a，b十进制之和，再判断进位
    def addBinary(self, a, b):
        sum_ab = int(a) + int(b)

        carry = 0
        res = ""
        div = sum_ab
        for _ in range(max(len(a), len(b))):
            remain = div % 10 + carry
            div = div // 10
            if remain >= 2:
                res = str(remain % 2) + res
                carry = 1
            else:
                res = str(remain) + res
                carry = 0
        return '1' + res if carry else res

    #构造a，b长度相等,然后再运算
    def addBinary2(self, a, b):
        l_a, l_b = len(a), len(b)
        l_max = max(l_a, l_b)
        a, b = (l_max - l_a)*'0' + a, (l_max - l_b)*'0' + b

        carry = 0
        res = ""
        for i in range(l_max - 1, -1, -1):
            int_a, int_b = int(a[i]), int(b[i])
            res = str((int_a + int_b + carry) % 2) + res
            carry = (int_a + int_b + carry) // 2
        return '1' + res if carry else res 
    

a = "1010"
b = "1011"
solute = Solution()
res = solute.addBinary2(a, b)
print(res)
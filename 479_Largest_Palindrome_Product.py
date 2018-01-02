#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 479_Largest_Palindrome_Product.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路，暴力解法, TLE
    #可以把i*j变为减法。但是时间复杂度不变
    def largestPalindrome(self, n):
        res = 0
        for i in range(10**n - 1, 10 ** (n - 1), -1):
            for j in range(10**n - 1, 10 ** (n - 1), -1):
                p = i * j
                if p < res:
                    break
                s = str(p)
                if s == s[::-1]:
                    res = p
        return res%1337

    #找规律题。。
    #当n为偶数时，比如4，10001 * 9999 = 99999999，最大数就为(10001-100)*9999

    #设两个数为n1 = 10**n - i，n2 = 10**n - j
    #所以n1*n2 = 10**n * (10**n - i - j) + i*j
    #upper = 10**n-i-j, lower = i*j
    #因为i * j < 10^N(不知道从哪里来的结论), 所以upper是前n位，i*j是后n位。
    #所以当lower是upper的翻转时，则为回文
    #因为当upper越大时，结果越大，所以把upper作为迭代的对象。另a=i+j
    #所以upper = 10**n-a，lower = a*i - i*i
    #reverse(upper) = a*i - i*i
    #=> i = (a*a/4 - reverse(upper))**0.5 + a/2
    #若i有整数解，则有解
    #即 (a*a - 4*reverse(upper))**0.5是整数，则有解

    def largestPalindrome2(self, n):
        if n == 1: return 9
        p = 10 ** n
        a, a_max = 2, 10**(n-1)*9
        #这里a用range的话，会MLE。。
        while a < a_max:
            upper = p - a
            lower = int(str(upper)[::-1])
            tmp = a*a - lower * 4
            a += 1
            if tmp < 0:
                continue
            #解i
            i = tmp**0.5
            if i == int(i):
                return (upper * p + lower) % 1337
        return 0



solute = Solution()
res = solute.largestPalindrome2(8)
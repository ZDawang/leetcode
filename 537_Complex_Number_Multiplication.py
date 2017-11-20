#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 537_Complex_Number_Multiplication
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def complexNumberMultiply(self, a, b):
        a_cut = a.split("+")
        a_real = int(a_cut[0])
        a_imag = int(a_cut[1][:-1])
        b_cut = b.split("+")
        b_real = int(b_cut[0])
        b_imag = int(b_cut[1][:-1])
        res_real = a_real*b_real - a_imag*b_imag
        res_imag = a_imag*b_real + a_real*b_imag
        return str(res_real) + "+" + str(res_imag) + "i"
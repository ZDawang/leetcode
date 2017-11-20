#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 552_Student_Attendance_Record_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #有两个条件，一个是有两个A，一个是有两个连续LL
    #两个A的情况是末尾一个A，前面一个A，两个连续LL的情况是末尾3个连续LL
    #去除这两种情况即可
    #所有有：
    #notA_P 前面不包含A，末尾是P
    #notA_L 前面不包含A，末尾是L
    #notA_LL 前面不包含A，末尾是LL
    #notA_A 前面不包含A，末尾是A
    #A_L 前面包含A，末尾是L
    #A_LL 前面包含A，末尾是LL
    #A_P 前面包含A，末尾是P
    #总共7种情况
    #时间复杂度O(n)
    def checkRecord(self, n):
        A_L, A_LL, A_P, notA_A, notA_L, notA_LL, notA_P = 0, 0, 0, 1, 1, 0, 1
        MOD = 1000000007
        for i in range(1, n):
            curA_L = (notA_A + A_P) % MOD
            curA_LL = A_L
            curA_P = (A_L + A_LL + notA_A + A_P) % MOD
            curnotA_A = (notA_L + notA_LL + notA_P) % MOD
            curnotA_L = notA_P
            curnotA_LL = notA_L
            curnotA_P = (notA_L + notA_LL + notA_P) % MOD
            A_L, A_LL, A_P, notA_A, notA_L, notA_LL, notA_P = curA_L, curA_LL, curA_P, curnotA_A, curnotA_L, curnotA_LL, curnotA_P
        return sum([A_L, A_LL, A_P, notA_A, notA_L, notA_LL, notA_P]) % MOD


    #logn  orz
    #所以是不是所有可以转移的都可以这样做了。。
    #若只关于dp内部可以转移，而不用把nums或其它的加进来，可以。
    def checkRecord2(self, n):
        A = np.matrix([[0, 0, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1],
                       [0, 0, 1, 1, 0, 1],
                       [0, 0, 1, 0, 1, 1]])
        power = A
        mod = 10**9 + 7
        while n:
            if n & 1:
                power = (power * A) % mod
            A = A**2 % mod
            n /= 2
        return int(power[5, 2])






solute = Solution()
res = solute.checkRecord(99999)


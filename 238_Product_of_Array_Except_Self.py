#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 238_Product_of_Array_Except_Self
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #[1,2,3,4] 对于2来说，结果为1*3*4，可以分为1*（3*4）也就是可以分为两部分。
    #即[1,1,2,6] 与 [24, 12, 4, 1]相乘
    #TLE
    def productExceptSelf(self, nums):
        #正向乘
        l = len(nums)
        l_res = [1]
        l_temp = 1
        for i in range(1, l):
            l_temp *= nums[i - 1]
            l_res.append(l_temp)
        #反向乘法
        r_res = [1]
        r_temp = 1
        for i in range(l - 1, 0, -1):
            r_temp *= nums[i]
            r_res = [r_temp] + r_res
        res = []
        for i in range(l):
            res.append(l_res[i] * r_res[i])
        return res

    #优化,将r_res， l_res， res放在一起， insert步骤去掉。
    def productExceptSelf2(self, nums):
        l = len(nums)
        #反向乘法
        res = []
        l_temp = 1
        for i in range(l):
            res.append(l_temp)
            l_temp *= nums[i]

        product_temp = 1
        for i in range(l - 1, -1, -1):
            res[i] *= product_temp
            product_temp *= nums[i]
        return res




nums = [1,2,3,4]
solute = Solution()
res = solute.productExceptSelf2(nums)
print(res)

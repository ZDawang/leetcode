#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 540_Single_Element_in_a_Sorted_Array
#time_complecity:  
#space_complecity: 
#beats: 

from functools import reduce
class Solution(object):
    #讲所有数进行亦或操作， O(n)
    def singleNonDuplicate(self, nums):
        return reduce(lambda x, y: x ^ y, nums, 0)

    #O(logn)
    #肯定需要二分法
    #如果一个数前面都是正常的(不包含它自己)。若它的下标是奇数，则它会与它前面的一个数相同。
    #若下标是偶数，则它会与它前面的一个数不同。
    def singleNonDuplicate2(self, nums):
        #判断一个数前面是否是正常的。不包含自己的原因是，当m为偶数时，不能判断它本身是否正常。
        def is_normal(m):
            return (m & 1 and nums[m] == nums[m - 1]) or (not m & 1 and nums[m] != nums[m - 1])

        l, r = 0, len(nums) - 1
        while l < r - 1:
            m = (l + r)//2
            #因为只能判断m之前正常，不能判断m是否正常，所以l=m
            if is_normal(m):
                l = m
            else:
                r = m
        return nums[r] if is_normal(r) else nums[l]


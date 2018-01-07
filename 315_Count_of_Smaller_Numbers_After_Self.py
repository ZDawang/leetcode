#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 315_Count_of_Smaller_Numbers_After_Self
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #暴力解法为O(N2)
    #但是有很多比较是重复的。
    
    #需要一种数据结构，查找与增加都是O(logn)的复杂度。
    #在新遍历一个数以后，需要查找比它小的元素有几个。需要把当前数字加入到结构中。
    #可以将增加变为更新。数组用来存储数字的数量。
    #BIT，新建一个BIT数组，数组中的值用来存储当前数字有几个。
    #插入时，就是将BIT数组中当前数字的数量加1。查找就是查找0到当前数字下标的和。
    #时间复杂度O(nlogn)
    def countSmaller(self, nums):
        #BIT
        class BIT(object):
            def __init__(self, l):
                self.l = l
                self.tree = [0] * self.l

            def update(self, i):
                while i < self.l:
                    self.tree[i] += 1
                    i += self.lowBit(i + 1)

            def lowBit(self, i):
                return i & (-i)

            def sumRange(self, i):
                sumi = 0
                while i >= 0:
                    sumi += self.tree[i]
                    i -= self.lowBit(i + 1)
                return sumi


        newNums = sorted(list(set(nums)))
        #查找数字的下标。
        loc = {num: i for i, num in enumerate(newNums)}
        #res
        res = [0] * len(nums)
        #BIT
        bit = BIT(len(newNums))
        #遍历
        for i in range(len(nums) - 1, -1, -1):
            index = loc[nums[i]]
            #当不是最小数时
            if index != 0:
                res[i] = bit.sumRange(index - 1)
            #更新BIT
            bit.update(index)
        return res

nums = [5, 2, 6, 1]
solute = Solution()
res = solute.countSmaller(nums)

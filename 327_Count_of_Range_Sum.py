#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 327_Count_of_Range_Sum.py
#time_complecity:  
#space_complecity: 
#beats: 
import bisect
class Solution(object):
    #O(n2)思路，dp存储到0到i的范围和，再遍历
    #TLE
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        dp = [0] * n
        res = 0
        for i in range(n):
            dp[i] = dp[i - 1] + nums[i]
        for i in range(n):
            for j in range(i, n):
                tmp = dp[j] if i == 0 else dp[j] - dp[i - 1]
                if lower <= tmp <= upper:
                    res += 1
        return res


#优化
#O(nlogn)
#可以将i之前的dp[i]进行排序。可是没有排序算法一次插入是logn的。。除非用红黑树或者二叉搜索树

#可以先排序，将未排序的数字依次放入排序后的位置。再用BIT计算在某个范围内的数字已经有多少。

#比如 已经放入的数字有 [2, x, 6, x, x, 8, 10, x, x, x], 这时我们需要找小于8的数字有多少个，那么就可以用二分找到8的位置，
#然后使用BIT来计算0到8有多少数字。

#BIT数组用来存放0与1，1代表已经出现过，因此BIT的sum操作，求的是比它小的数有多少个。


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        bit = [0] * (n + 2)

        def lowbit(i):
            return i & (-i)

        def update(i):
            while i <= n + 1:
                bit[i] += 1
                i += lowbit(i + 1)

        def sumRange(i):
            cnt = 0
            while i >= 0:
                cnt += bit[i]
                i -= lowbit(i + 1)
            return cnt

        n = len(nums)
        sums = [0] * (n + 1)
        #sums
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        #排序
        sortSums = sorted(sums)

        res = 0
        for sumNum in sums:
            #找到在[sumNum - lower, sumNum - upper]范围 在sortNums中的左右边界。
            #较大的数为右边界，较小的数为左边界。
            l = bisect.bisect_left(sortSums, sumNum - upper) - 1
            r = bisect.bisect_right(sortSums, sumNum - lower) - 1
            res += sumRange(r) - sumRange(l)
            #寻找插入位置，更新bit
            idx = bisect.bisect_left(sortSums, sumNum)
            update(idx)
        return res






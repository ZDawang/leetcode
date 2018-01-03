#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-27
#difficulty degree：
#problem: 632_Smallest_Range
#time_complecity:  
#space_complecity: 
#beats: 

import heapq

class Solution(object):
    #第一思路，将nums的每个list都拿一个到堆中。每次找最小的那个，将它替换成它所在的list的下一个数字。
    #直到有list遍历完。
    #所有这个buffer可以用堆来完成。堆里存放数字以及数字所属的list序号以及数字在list中的位置。
    #时间复杂度 O(logk)*sum(len(l) for l in nums)
    def smallestRange(self, nums):
        heap = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(heap)
        #标记当前heap中的最大数。
        maxnum = max(h[0] for h in heap)
        #用来标记当前最小数在哪个list中的哪个位置。
        minnum, minlist, minloc = heapq.heappop(heap)
        res_min, res_max = minnum, maxnum
        #判断最小数所在list是否遍历完
        while minloc + 1 != len(nums[minlist]):
            #向堆中加入新数
            heapq.heappush(heap, (nums[minlist][minloc + 1], minlist, minloc + 1))
            maxnum = max(maxnum, nums[minlist][minloc + 1])
            #获取堆中最小数
            minnum, minlist, minloc = heapq.heappop(heap)
            #更新res
            if res_max - res_min > maxnum - minnum:
                res_max, res_min = maxnum, minnum
        return [res_min, res_max]


    #思路2：discuss中的滑动窗。
    

nums = [[1,2,3],[1,2,3],[1,2,3]]
solute = Solution()
res = solute.smallestRange2(nums)
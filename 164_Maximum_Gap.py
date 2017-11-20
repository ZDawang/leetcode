#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 164_Maximum_Gap.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #桶排序。因为maxgap >= ceil((maxnum - minnum)/N) 所以需要N个桶即可。
    def maximumGap(self, nums):
        l = len(nums)
        if l < 2: return 0
        minnum, maxnum = min(nums), max(nums)
        #gap是(maxnum - minnum)/N 向上取整
        div, remain = divmod(maxnum - minnum, l)
        gap = div if remain == 0 else div + 1
        #定义桶
        minbucket = [float("inf")] * l
        maxbucket = [float("-inf")] * l

        #将数放入桶中
        for num in nums:
            #把最大的数放入最后一个桶中
            if num == maxnum:
                minbucket[-1], maxbucket[-1] = maxnum, maxnum
                continue
            index = (num - minnum)//gap
            minbucket[index] = min(minbucket[index], num)
            maxbucket[index] = max(maxbucket[index], num)
        #从桶中获得结果
        maxgap, premax = float("-inf"), minnum
        for i in range(l):
            if minbucket[i] == float("inf") and maxbucket[i] == float("-inf"):
                continue
            maxgap = max(maxgap, minbucket[i] - premax)
            premax = maxbucket[i]
        return maxgap

nums = [1, 3, 100]
solute = Solution()
res = solute.maximumGap(nums)


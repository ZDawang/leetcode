#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 475_Heaters.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路：贪心算法。对于每个房子，都找到离它最近的heater，计算距离。
    #则结果就是最大的距离。
    #使用双指针
    #时间复杂度，O(max(nlogn, mlogm))
    def findRadius(self, houses, heaters):
        p, res = 0, 0
        houses.sort()
        heaters.sort()
        for house in houses:
            while p < len(heaters) - 1 and abs(house - heaters[p]) >= abs(house - heaters[p + 1]):
                p += 1
            res = max(res, abs(house - heaters[p]))
        return res


    #贪心算法，不过由双指针改为二分查找。
    #对每个房子都进行二分查找。找到最小的距离。
    #时间复杂度O(max(mlogm, nlogm))
    def findRadius2(self, houses, heaters):
        #查找比house大的的heater位置。
        def Binsearch(heaters, house):
            if house > heaters[-1]: return -1
            l, r = 0, len(heaters) - 1
            while l < r:
                m = l + (r - l)//2
                if heaters[m] > house:
                    r = m
                else:
                    l = m + 1
            return l

        heaters.sort()
        res = 0
        for house in houses:
            index = Binsearch(heaters, house)
            #查找到的heater位置，可能在最尾部或者开头或者中间。
            if index == -1:
                res = max(res, house - heaters[-1])
            elif index == 0:
                res = max(res, heaters[0] - house)
            else:
                res = max(res, min(house - heaters[index - 1], heaters[index] - house))
        return res


houses = [i for i in range(50)]
heaters = [i for i in range(50)]

solute = Solution()
res = solute.findRadius(houses, heaters)
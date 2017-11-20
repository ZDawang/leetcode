#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 658_Find_K_Closest_Elements.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #二分法，找到使x-arr[i] <= arr[i+k]-x的最小i值
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r)//2
            #说明arr[m]太小，且m不满足条件，因此l=m+1
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l: l + k]


    #双指针
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            if arr[right] - x >= x - arr[left]:
                right -= 1
            else:
                left += 1
        return arr[left: right + 1]
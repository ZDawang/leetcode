#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-7
#difficulty degree：
#problem: 75_sort_colors
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    # 将0向前放，2向后放，1不管
    def sortColors(self, nums):
        len_nums = len(nums)
        l, r = 0, len_nums - 1
        for i in range(len_nums):
            if nums[i] == 0:
                l += 1
            else:
                break
        for j in range(len_nums - 1, -1, -1):
            if nums[j] == 2:
                r -= 1
            else:
                break
        temp = l
        while(temp <= r):
            while(nums[temp] != 1 and l <= r and temp <= r):
                if nums[temp] == 0:
                    if temp == l:
                        l += 1
                        temp += 1
                    else:
                        nums[l], nums[temp] = nums[temp], nums[l]
                        l += 1
                else:
                    nums[r], nums[temp] = nums[temp], nums[r]
                    r -= 1
            temp += 1

nums = [2,0]
solute = Solution()
solute.sortColors(nums)
print(nums)

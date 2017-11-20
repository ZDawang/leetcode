#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 11_container_with_most_water
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def maxArea(self, height):
		#从两边向中间寻找。因为每次只动一个边，所以选择边最大的不动即可:因为目的是为了寻找较长的两个边，而不是使用贪心算法
		left = 0
		right = len(height) - 1

		volume = min(height[left], height[right]) * (right - left)

		while(left<right):
			#更新边的位置
			(left,right) = (left + 1, right) if height[left] < height[right] else (left,right - 1) 
			#计算更新边位置后容量
			temp = min(height[left], height[right]) * (right - left)

			if volume < temp :
				volume = temp
		return volume


height = [11,6,8,55,1,20,10]
solute = Solution()
res = solute.maxArea(height)

print(res)

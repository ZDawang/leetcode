#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 384_Shuffle_an_Array.py
#time_complecity:  
#space_complecity: 
#beats: 


import random
class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        

    def reset(self):
        return self.nums
        
    #洗牌算法，因为一个元素挪过位置后，就不会再动了。
    #可知，所有元素到最后一个位置的概率为1/n，到倒数第二个元素的概率为
    #不能到最后一个位置，同时到倒数第二个位置。(n-1)/n*(1/(n-1)) = 1/n....
    #依次类推，所有元素到所有位置的概率均为1/n,
    def shuffle(self):
        res = self.nums.copy()
        #从后向前
        for i in range(len(ans) - 1, 0, -1):
            #从[0, i]中选择一个整数
            j = random.randint(0, i)
            res[i], res[j] = res[j], res[i]
        return res
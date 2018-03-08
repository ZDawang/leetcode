#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 398_Random_Pick_Index.py
#time_complecity:  
#space_complecity: 
#beats: 

import random
from collections import defaultdict
class Solution:
    def __init__(self, nums):
        self.d = defaultdict(list)
        for i, num in enumerate(nums):
            self.d[num].append(i)
        

    def pick(self, target):
        if not target in self.d:
            return None
        i = random.randrange(0, len(self.d[target]))
        return self.d[target][i]
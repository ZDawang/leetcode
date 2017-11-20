#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 458_Poor_Pigs
#time_complecity:  
#space_complecity: 
#beats: 


class Solution(object):
    #利用信息量来做
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        #the information of the posion bucket
        posionInfo = math.log(buckets, 2)
        #the information that we can get from a pig
        pigInfo = math.log(minutesToTest // minutesToDie + 1, 2)
        #so,the result..
        return int(math.ceil(posionInfo / pigInfo))



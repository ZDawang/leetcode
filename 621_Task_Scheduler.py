#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 621_Task_Scheduler.py
#time_complecity:  
#space_complecity: 
#beats: 

from collections import Counter
class Solution(object):
    #贪心算法。因为每两个相同的任务都需要间隔n，所以只需要考虑最大数量的那个或那些任务即可。
    #就是先放好数量最多的那个任务，然后在中间的间隙中，加入其它任务。
    #不过也有可能间隔非常小，放不下其它任务。此时不需要任何idle，所以最大interval就是任务数量。
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        max_task = max(count.values())
        max_num = sum(count[t] == max_task for t in count)
        return max(len(tasks), (n + 1)*max_task - n + max_num - 1)


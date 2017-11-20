#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 380_Insert_Delete_GetRandom_O(1)
#time_complecity:  
#space_complecity: 
#beats: 

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l, self.d = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.l.append(val)
            self.d[val] = len(self.l) - 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            idx, last = self.d[val], self.l[-1]
            self.l[idx], self.d[last] = last, idx
            self.l.pop(); self.d.pop(val, 0)
            return True
        return False
            
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.l[random.randint(0, len(self.l) - 1)]
#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-31
#difficulty degree：
#problem: 49_group_anagrams
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def groupAnagrams(self, strs):
        def sort_str(str_element):
            return "".join((lambda x:(x.sort(),x)[1])(list(str_element)))

        res = []
        d = {}
        i = 0
        for str_element in strs:
            sort_s = sort_str(str_element)
            print(sort_s, d)
            if sort_s in d:
                res[d[sort_s]] += [str_element]
            else:
                d[sort_s] = i
                i += 1
                res.append([str_element])
        return res

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solute = Solution()
res = solute.groupAnagrams(strs)

print(res)
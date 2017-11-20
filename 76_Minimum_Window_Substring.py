#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 76_Minimum_Window_Substring
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP
    def Isd1Ind2(self, d1, d2):
        for i in d1:
            if i not in d2:
                return False
            if d1[i] > d2[i]:
                return False
        return True

    def minWindow(self, s, t):
        dt = {}
        for t_element in t:
            dt[t_element] = dt.setdefault(t_element, 0) + 1
        st = {}
        stemp = ""
        len_stemp = 0
        res = ""
        len_res = len(s)
        for s_element in s:
            st[s_element] = st.setdefault(s_element, 0) + 1
            len_stemp += 1
            stemp += s_element
            while self.Isd1Ind2(dt, st):
                if len_stemp <= len_res:
                    res = stemp
                    len_res = len_stemp
                st[stemp[0]] -= 1
                stemp = stemp[1:]
                len_stemp -= 1
        return res

s = "aaaaaaaaaaaabbbbbcdd"
solute = Solution()
res = solute.minWindow(s, "abcdd")
print(res)
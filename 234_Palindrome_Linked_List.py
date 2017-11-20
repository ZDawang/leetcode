#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 234_Palindrome_Linked_List.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #改变链表结果，使后一半反向
    def isPalindrome(self, head):
        #获得链表长度
        l, p = 0, head
        while p:
            l, p = l + 1, p.next
        #反向
        pre, cur = None, head
        count = 0
        while cur:
            tmp = cur.next
            if count > l // 2:
                cur.next = pre
            pre, cur = cur, tmp
            count += 1
        #比较
        count = 0
        while count < l // 2:
            count += 1
            if not head.val == pre.val:
                return False
            head, pre = head.next, pre.next
        return True


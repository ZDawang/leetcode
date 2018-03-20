#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-6
#difficulty degree ：meidum
#problem:2_add_two_numbers
#time_complecity: O(n)
#space_complecity: O(n)
#beats: 40

#链表 属性有next，val
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_bit = 0
        root = res = ListNode(0)
        while l1 or l2 or carry_bit:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            res.next = ListNode((v1 + v2 + carry_bit)%10)
            carry_bit = (v1 + v2 + carry_bit)/10
            res = res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return root.next
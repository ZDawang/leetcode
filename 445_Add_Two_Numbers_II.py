#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 445_Add_Two_Numbers_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用栈，先入先出进行倒叙遍历
    def addTwoNumbers(self, l1, l2):
        #建立栈
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        #遍历
        num, carry, prenode = 0, 0, None
        while stack1 and stack2:
            num = stack.pop().val + stack2.pop().val + carry
            carry, num = divmod(num, 10)
            node = ListNode(num)
            prenode, node.next = node, prenode
        #选择没空的栈继续遍历
        stack = stack1 or stack2
        while stack:
            num = stack1.pop().val + carry
            carry, num = divmod(num, 10)
            node = ListNode(num)
            prenode, node.next = node, prenode
        if carry:
            node = ListNode(carry)
            prenode, node.next = node, prenode
        return prenode



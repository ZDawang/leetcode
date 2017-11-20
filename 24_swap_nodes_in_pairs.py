#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 23_swap_nodes_in_pairs
#time_complecity:  
#space_complecity: 
#beats: 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    #构造一个函数将列表加进链表中
    def list_append(self, nums):
        head = ListNode(nums[0])
        front = head
        for i in range(1,len(nums)):
            front.next = ListNode(nums[i])
            front = front.next
        return head
    def show(self):
        print(self.val)


class Solution(object):
    def swapPairs(self, head):
        if not head:
            return []
        if not head.next:
            return head
        res = head.next
        temp = ListNode(0)
        while head.next and head.next.next:
            temp.next = head.next.next
            head.next.next = head
            head.next = temp.next.next
            head_temp = head
            head = temp.next
        if not head.next:
            head_temp.next = temp.next
        else:
            head.next.next = head
            head.next = None
        return res

l1 = [1]

head_l1 = ListNode(1)
head_l1 = head_l1.list_append(l1)

solute = Solution()
res = solute.swapPairs(head_l1)

a = ListNode(1)
a.show()

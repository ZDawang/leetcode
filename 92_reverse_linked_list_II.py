#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-14
#difficulty degree：
#problem: 92_reverse_linked_list_II
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

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        for i in range(m - 1):
            pre = pre.next
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next_node, cur.next = cur.next, reverse
            reverse, cur = cur, next_node
        pre.next.next = cur
        pre.next = reverse
        return dummyNode.next

l1 = [1,2,3,4,5]
head = ListNode(1)
head = head.list_append(l1)
solute = Solution()
res = solute.reverseBetween(head, 2, 4)

while(res):
    print(res.val)
    res = res.next
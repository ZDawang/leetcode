#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-22
#difficulty degree：
#problem: 25_reverse_nodes_in_k_group
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
    def reverseKGroup(self, head, k):
        tail_front = head
        res = head.next
        while(1):
            if not head:
                return res
            tail = head
            tail_b = tail.next
            for i in range(k-1):
                if not tail_b:
                    return res
                tail.next = tail_b.next
                tail_b.next = head
                head = tail_b
                tail_b = tail.next
            tail_front.next = head
            tail_front = tail




l1 = [1,2,3,4,5,6]

head = ListNode(1)
head = head.list_append(l1)

tail = ListNode(0)

solute = Solution()
res = solute.reverseKGroup(head, 2)

while(res):
    print(res.val)
    res = res.next


def reverseKGroup(self, head, k):
    if not head:
        return False
    tail = head
    tail_b = tail.next
    for i in range(k-1):
        if not tail_b:
            return False
        tail.next = tail_b.next
        tail_b.next = head
        head = tail_b
        tail_b = tail.next
    return head
#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-6
#difficulty degree：
#problem: 61_rotate_list
#time_complecity:  
#space_complecity: 
#beats: 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def list_append(self, nums):
        head = ListNode(nums[0])
        front = head
        for i in range(1,len(nums)):
            front.next = ListNode(nums[i])
            front = front.next
        return head


class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return []
        #计算listnode长度
        l_list = ListNode(0)
        l_list.next = head
        l = 0
        while(l_list.next):
            l_list.next = l_list.next.next
            l += 1
        new1, new2 = ListNode(0), ListNode(0)
        new1.next, new2.next = head, head
        i = 1
        k = k % l
        while(head.next):
            if i - k > 0:
                new2.next = new2.next.next
            i += 1
            head = head.next
        head.next = new1.next
        res = ListNode(0)
        res.next = new2.next.next
        new2.next.next = None
        return res.next

l1 = [1, 2, 3, 4, 5]

head = ListNode(1)
head = head.list_append(l1)

solute = Solution()
res = solute.rotateRight(head, 5)

while(res):
    print(res.val)
    res = res.next
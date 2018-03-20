#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-12
#difficulty degree：
#problem: 82_remove_duplicates_from_sorted_list_II
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
    def deleteDuplicates(self, head):
        #判断列表长度小于3时的情况
        if not head or not head.next or not head.next.next:
            if not head:
                return None
            if not head.next:
                return head
            if head.val == head.next.val:
                return None
            return head
        res = start = ListNode(0)
        #判断开头两个数据
        if head.val != head.next.val:
            start.next = head
            start = start.next
        #处理第三个数据到倒数第二个
        while(head.next.next):
            if head.val != head.next.val and head.next.val != head.next.next.val:
                start.next = head.next
                start = start.next
                head = head.next
            else:
                head = head.next
        #处理最后两个数据
        if head.val != head.next.val:
            start.next = head.next
        else:
            start.next = None
        return res.next


    def deleteDuplicates2(self, head):
        if not head or not head.next:
            return head
        pre, cur = ListNode(float("inf")), head
        res, pre.next = pre, head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return res.next



l1 = [1,2,2]

head = ListNode(1)
head = head.list_append(l1)
solute = Solution()
res = solute.deleteDuplicates(head)

while(res):
    print(res.val)
    res = res.next

                    

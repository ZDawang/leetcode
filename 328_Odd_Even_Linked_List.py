#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 328_Odd_Even_Linked_List
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #用两个指针分别代表奇数位的节点与偶数位的节点。
    #将链表分为三个小链表，第一个是奇节点链表，第二个是偶节点链表，第三个是未处理链表。
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd, even, start = head, head.next, head.next.next
        evenStart, oddoreven = even, 0
        while start:
            #若为偶数节点
            if oddoreven:
                even.next = start
                even, start = even.next, start.next
            else:
                odd.next = start
                odd, start = odd.next, start.next
            oddoreven = 1 - oddoreven
        #将偶数链后面置空，奇数节点后面连接偶数链起始节点。
        even.next, odd.next = None, evenStart
        return head



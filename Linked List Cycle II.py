#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        if head.next is None:
            return None
        
        iscyc = False
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while slow != fast:
                    fast, slow = fast.next, slow.next
                return slow
        return None
        
if __name__ == "__main__":
    

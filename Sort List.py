#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        def merge(h1, h2):
            hn = ListNode(-100000000)
            c = hn
            while h1 is not None and h2 is not None:
                if h1.val < h2.val:
                    c.next = h1
                    h1 = h1.next
                else:
                    c.next = h2
                    h2 = h2.next
                c = c.next
            if h1 is not None:
                c.next = h1
            if h2 is not None:
                c.next = h2
            return hn.next

        if head is None or head.next is None:
            return head
        f = head.next.next
        p = head
        while f is not None and f.next is not None:
            p = p.next
            f = f.next.next
        h2 = self.sortList(p.next)
        p.next = None
        return merge(self.sortList(head), h2)
        
        
if __name__ == "__main__":
    

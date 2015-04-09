#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        cur = head
        while cur is not None:
            nxt = cur.next
            new = RandomListNode(cur.label)
            cur.next = new
            new.next = nxt
            cur = nxt

        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        pHead = RandomListNode(0)
        newCur = pHead

        while cur is not None:
            nxt = cur.next.next

            new = cur.next
            newCur.next = new
            newCur = new

            cur.next = nxt

            cur = nxt

        return pHead.next

if __name__ == "__main__":
    sol = Solution()

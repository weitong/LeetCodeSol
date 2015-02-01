#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

# Definition for singly-linked list.
import tools
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        p = st = head
        cur = st.next
        while cur:
            if cur.val <= head.val:
                st.next = cur.next
                cur.next = head
                head = cur
            else:
                # Key Step: speculation
                if p.val > cur.val:
                    p = head

                # Key Step: reduce the judgement condition of the while statement
                while p.next.val < cur.val:
                    p = p.next
                if p == st:
                    st = cur
                else:
                    st.next = cur.next
                    cur.next = p.next
                    p.next = cur
                    
            cur = st.next
        return head
            

if __name__ == "__main__":
    sol = Solution()
    def cons(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        prev = head
        for i in range(1, len(lst)):
            prev.next = ListNode(lst[i])
            prev = prev.next
        prev.next = None
        return head

    def output(head):
        cur = head
        while cur is not None:
            print cur.val,
            cur = cur.next
        print '\n'

    import data
    a = cons([4,2,1,3]) 
    output(a)
    import time
    begin = time.time()
    b = sol.insertionSortList(a)
    print time.time() - begin
    output(b)

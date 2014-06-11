#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
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
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            merge = []
            head1, head2 = l1, l2
            while head1 is not None and head2 is not None:
                if head1.val <= head2.val:
                    merge.append(head1.val)
                    head1 = head1.next
                else:
                    merge.append(head2.val)
                    head2 = head2.next
            
            if head2 is not None:
                while head2 is not None:
                    merge.append(head2.val)
                    head2 = head2.next
            elif head1 is not None:
                while head1 is not None:
                    merge.append(head1.val)
                    head1 = head1.next
            else:
                pass
            return cons(merge)

if __name__ == "__main__":
    sol = Solution()
    from tools import consList, outputList
    la = consList([2])
    lb = consList([1])
    c = sol.mergeTwoLists(la, lb)
    outputList(c)

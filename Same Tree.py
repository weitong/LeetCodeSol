#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        def tEqual(n1, n2):
            if n1 is None and n2 is None:
                return True
            elif n1 is None:
                return False
            elif n2 is None:
                return False
            else:
                if tEqual(n1.left, n2.left) and tEqual(n1.right, n2.right):
                    if n1.val == n2.val:
                        return True
                    else:
                        return False
                else:
                    return False
                    
        return tEqual(p, q)


class WrongSolution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        def preorder(node):
            if node is None:
                return []
                
            if node.left is None and node.right is None:
                return [node.val]
            elif node.left is None:
                return [node.val] + preorder(node.right)
            elif node.right is None:
                return preorder(node.left) + [node.val]
            else:
                return preorder(node.left) + [node.val] + preorder(node.right)
                
        def inorder(node):
            if node is None:
                return []
                
            if node.left is None and node.right is None:
                return [node.val]
            elif node.left is None:
                return [node.val] + inorder(node.right)
            elif node.right is None:
                return [node.val] + inorder(node.left)
            else:
                return [node.val] + inorder(node.left) + inorder(node.right)
        
        def lq(l1, l2):
            if len(l1) != len(l2):
                return False
            else:
                for i in range(len(l1)):
                    if l1[i] != l2[i]:
                        return False
                            
                return True

        preorder_p, preorder_q = preorder(p), preorder(q)
        inorder_p, inorder_q = inorder(p), inorder(q)
        
        return lq(preorder_p, preorder_q) and lq(inorder_p, inorder_q)

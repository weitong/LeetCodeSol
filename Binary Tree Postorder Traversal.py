#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return []
        
        stack = [root]
        result = []
        while stack:
            cur = stack.pop()
            if not isinstance(cur, TreeNode):
                result.append(cur)
                continue

            stack.append(cur.val)
            
            if cur.right is not None:
                stack.append(cur.right)
            
            if cur.left is not None:
                stack.append(cur.left)

            
            
        return result
            
                
        

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    sol = Solution()
    print sol.postorderTraversal(n1)

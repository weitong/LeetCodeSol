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
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        result = []
        level = [root]
        while True:
            if not level or level[0] is None:
                break

            nxtLevel = []
            curValues = []
            for nd in level:
                curValues.append(nd.val)
                if nd.left is not None:
                    nxtLevel.append(nd.left)
                if nd.right is not None:
                    nxtLevel.append(nd.right)
            result.insert(0, curValues)
            level = nxtLevel
        return result
    
if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(3)
    n7 = TreeNode(4)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n5.left = n6
    n6.left = n7
    
    sol = Solution()
    print sol.levelOrderBottom(n1)
    

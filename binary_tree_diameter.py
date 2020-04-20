"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root):
            
            nonlocal maxDiameter
            if not root: 
                return 0
            left = depth(root.left)
            right = depth(root.right)
            
            #get the no of edges in both children
            currentDiameter = left + right
            
            #track max diameter
            maxDiameter = max(maxDiameter, currentDiameter)
            
            #we can only return one of the children
            #we add a one to represent the edge 
            #between node and parent above
            return max(left, right) + 1
        
        maxDiameter = 0
        depth(root)
        return maxDiameter

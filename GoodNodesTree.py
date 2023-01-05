# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Solution 1 - using extra array space

        # res = []
        # def dfs(root, maxVal):

        #     if root:

        #         if root.val >= maxVal:
        #             res.append(root.val)

        #         dfs(root.left, max(root.val, maxVal))
        #         dfs(root.right, max(root.val, maxVal))
            
        # dfs(root, root.val)
        # return len(res)


        # Solution 2 - without using extra array space.

        if not root:
            return 0


        def dfs(root, maxVal):
            if not root:
                return 0

            res = 0
            if root.val >= maxVal:
                res += 1

            res += dfs(root.left, max(root.val, maxVal))
            res += dfs(root.right, max(root.val, maxVal))
            return res
            
        return dfs(root, root.val)
        
        
        
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.



#Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.


# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

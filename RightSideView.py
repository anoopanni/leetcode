# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        from collections import deque 
        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                p = q.popleft()
                if p:
                    if p.right:
                        q.append(p.right)
                    if p.left:
                        q.append(p.left)
                    if i==0:
                        res.append(p.val)
        return res
      
      
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]


# Input: root = [1,null,3]
# Output: [1,3]


# Input: root = []
# Output: []

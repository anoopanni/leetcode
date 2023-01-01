# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #DFS - Depth first Search has three main types: 
        # 1. Pre-Order Traversal (root-left-right)
        # 2. In-Order Traversal (left-root-right)
        # 3. Post-Order Traversal (left-right-root)
        
        # 1. Pre-Order 
        if root:
            print(root.val)
            self.invertTree(root.left)
            self.invertTree(root.right)

        # 2. In-Order 
        # if root:
        #     self.invertTree(root.left)
        #     print(root.val)
        #     self.invertTree(root.right)

        # 3. Post-Order
        # if root:
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        #     print(root.val)


        # DFS using Stack DataStructure

        # if not root:
        #     return

        # s = []
        # s.append(root)

        # while s:
        #     popped = s.pop()
        #     print(popped.val)
        #     if popped.right:
        #         s.append(popped.right)
        #     if popped.left:
        #         s.append(popped.left)


        # BFS using queue DataStructure

        # if not root:
        #     return 

        # from collections import deque

        # q = deque()
        # q.append(root)

        # while q:
        #     popped = q.popleft()
        #     print(popped.val)
        #     if popped.left:
        #         q.append(popped.left)
        #     if popped.right:
        #         q.append(popped.right)

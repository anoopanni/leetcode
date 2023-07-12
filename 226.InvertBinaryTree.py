# https://leetcode.com/problems/invert-binary-tree/description/
# 226. Invert Binary Tree


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
        # if root:
        #     print(root.val)
        #     # root.left, root.right = root.right, root.left # Inverting
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        #     # root.left, root.right = root.right, root.left # Inverting
        # return root

        # 2. In-Order 
        # if root:
        #     root.left, root.right = root.right, root.left # Inverting
        #     self.invertTree(root.left)
        #     print(root.val)
        #     self.invertTree(root.right)
        # return root

        # 3. Post-Order
        # if root:
        #     root.left, root.right = root.right, root.left # Inverting
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        #     print(root.val)
        # return root



        # DFS using stack data structure


        # st = [root]

        # while st:
        #     popped = st.pop()
        #     if popped:
        #         # print(popped.val)
        #         popped.left, popped.right = popped.right, popped.left # Inverting
        #         st.append(popped.left)
        #         st.append(popped.right)
        
        # return root

        
        # BFS using stack data structure

        from collections import deque 

        q = deque([root])

        while q:
            popped = q.popleft()
            if popped:
                # print(popped.val)
                popped.left, popped.right = popped.right, popped.left # Inverting
                q.append(popped.left)
                q.append(popped.right)

        return root





# Example 1:

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]


# Example 2:

# Input: root = [2,1,3]
# Output: [2,3,1]


# Example 3:

# Input: root = []
# Output: []
        

        

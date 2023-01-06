# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recursive(node, left, right):
            if not node:
                return True
            
            if not (right > node.val > left):
                return False
            
            return recursive(node.left, left, node.val) and recursive(node.right, node.val, right)
        
        return recursive(root, float('-inf'), float('inf'))
        


# Input: root = [2,1,3]
# Output: true
  
  
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

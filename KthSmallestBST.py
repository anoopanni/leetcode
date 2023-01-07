# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        # Recursive Solution

        # res = []

        # def recursive(root):

        #     if root:
        #         recursive(root.left)
        #         res.append(root.val)
        #         recursive(root.right)

        # recursive(root)

        # return res[k-1]


        # Iterative Solution - How to do pre-order traversing iteratively (******)

        st = []
        res = []

        cur = root

        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left

            p = st.pop()
            res.append(p.val)

            cur = p.right


        return res[k-1]
            
        
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
  

                
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3




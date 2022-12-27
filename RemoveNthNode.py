# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # Recursive Solution 
        count = n
        def traverse(first):
            # print(first.val)
            if first.next:
                traverse(first.next)
            nonlocal count
            if count == 0:
                first.next = first.next.next
            count -= 1
            return first

        return traverse(dummy).next


        # Iterative Solution 

#         first = dummy
#         second = head

#         while(n):
#             n -= 1
#             second = second.next

    
#         while second:
#             first = first.next
#             second = second.next

#         first.next = first.next.next

#         return dummy.next
      
      
#test case:
# Input
# head =
# [1,2,3,4,5]
# n =
# 2
# Output
# [1,2,3,5]
# Expected
# [1,2,3,5]


# Input
# head =
# [1]
# n =
# 1
# Output
# []
# Expected
# []


# Input
# head =
# [1,2]
# n =
# 1
# Output
# [1]
# Expected
# [1]


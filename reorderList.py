# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None



        prev = None
        temp = None
        while second != None:
            temp = second.next
            # second.next.next = second
            second.next = prev
            prev = second
            second = temp

        # Printing the reversed linked list
        # while prev != None:
        #     print(prev.val)
        #     prev = prev.next

        

        # Join linkedlist prev and head to form a new linkedlist

        left, right = head, prev


        while right != None:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2

        return left
      
     

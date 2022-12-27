# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        
        rMap = {}

        HeadMap = head
        while HeadMap:
            newNode = Node(HeadMap.val, None, None)
            rMap[HeadMap] = newNode
            HeadMap = HeadMap.next

        
        traverse = head
        while traverse:
            if traverse.next:
                rMap[traverse].next = rMap[traverse.next]
            if traverse.random:
                rMap[traverse].random = rMap[traverse.random]
            else:
                rMap[traverse].random = None
            traverse = traverse.next

        return rMap[head]
        
        
# test case:
#  Input
# [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output
# [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Expected
# [[7,null],[13,0],[11,4],[10,2],[1,0]]



# Input
# [[1,1],[2,1]]
# Output
# [[1,1],[2,1]]
# Expected
# [[1,1],[2,1]]



# Input
# [[3,null],[3,0],[3,null]]
# Output
# [[3,null],[3,0],[3,null]]
# Expected
# [[3,null],[3,0],[3,null]]

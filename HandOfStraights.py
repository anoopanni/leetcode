# 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights/description/

import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        count = {}

        for i in range(len(hand)):
            count[hand[i]] = count.get(hand[i], 0) + 1
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1

                if count[i] == 0:
                    if minH[0] != i:
                        return False
                    heapq.heappop(minH)

        return True


# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
  
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.



        

 


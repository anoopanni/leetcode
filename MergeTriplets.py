# 1899. Merge Triplets to Form Target Triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seen_target = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                    continue 
                    
            # for i in range(3):
            #     if t[i] == target[i]:
            #         seen_target.add(t[i])
            
            for i,v in enumerate(t):
                if v == target[i]:
                    seen_target.add(i)

        # return len(seen_target) == len(set(target))
                
        return len(seen_target) == 3
      

      
# Example 1:

# Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
# Output: true
# Explanation: Perform the following operations:
# - Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
# The target triplet [2,7,5] is now an element of triplets.

# Example 2:

# Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
# Output: false
# Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
  
# Example 3:

# Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
# Output: true
# Explanation: Perform the following operations:
# - Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
# - Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
# The target triplet [5,5,5] is now an element of triplets.

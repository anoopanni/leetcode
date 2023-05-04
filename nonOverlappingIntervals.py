# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Solution 1 - Greedy approach

        # intervals.sort()
        # res = [intervals[0]]
        # count = 0


        # for i in range(1, len(intervals)):
        #     if res[-1][1] > intervals[i][0]:
        #         res[-1][1] = min(intervals[i][1], res[-1][1])
        #         count += 1
        #     else:
        #         res.append(intervals[i])
        

        # return count



        # Solution 2 - Space optimised

        intervals = sorted(intervals, key = lambda x: x[0])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                prevEnd = min(intervals[i][1], prevEnd)
                res += 1 
            else:
                prevEnd = intervals[i][1]

        return res

      
# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
  
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
  
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

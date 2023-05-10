# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/description/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        # start.sort()

        end = sorted([x[1] for x in intervals])
        # end.sort()

        res, count = 0, 0
        i, j = 0, 0

        while i < len(intervals):

            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)

        return res
      
      
      
# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
  
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

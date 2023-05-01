# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/description/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # Solution 1

        # intervals = sorted(intervals, key=lambda x:x[0])

        # for i in range(len(intervals)-1):
        #     if intervals[i][0] <= intervals[i+1][0] < intervals[i][1]:
        #         return False

        # return True


        # Solution 2 

        intervals = sorted(intervals, key=lambda x:x[0])

        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False

        return True


      

      
# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
  
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true

#https://leetcode.com/problems/target-sum/description/
#494. Target Sum

class Solution:
    def __init__(self):
        self.seen = dict()

    def backTrack(self, nums, target, track):
        if track in self.seen:
            return self.seen[track]

        if track[0] == len(nums) and track[1] == target:
            return 1
        if track[0] >= len(nums):
            return 0

        # Left side of the tree; postive numbers      
        res1 = self.backTrack(nums, target, (track[0] + 1, track[1] + nums[track[0]]))
        # Left side of the tree; negative numbers   
        res2 = self.backTrack(nums, target, (track[0] + 1, track[1] + (-nums[track[0]]))) 
        result = res1 + res2

        self.seen[track] = result

        return result



    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.backTrack(nums, target, (0, 0))



#input
#nums =
#[1,1,1,1,1]
#target =
#3
#Output
#5
#Expected
#5

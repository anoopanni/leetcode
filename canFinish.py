# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = collections.defaultdict(list)
        visit = set()

        for crs in prerequisites:
            adjMap[crs[0]].append(crs[1])

        
        def dfs(crs):

            if not adjMap[crs]:
                return True
            
            if crs in visit:
                return False

            visit.add(crs)
            
            for each_crs in adjMap[crs]:
                if not dfs(each_crs):
                    return False
            
            visit.remove(crs)
            adjMap[crs] = []

            return True


        for crs in prerequisites:
            if not dfs(crs[0]):
                return False

        return True



# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        # DEPTH FIRST SEARCH - RECURSIVE
        def dfs(r, c):

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for inc_r, inc_c in directions:
                new_r, new_c = r + inc_r, c + inc_c

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == "1" and (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    dfs(new_r, new_c)


        # BREADTH FIRST SEARCH and DEPTH FIRST SEARCH - ITERATIVE
        def bfs_dfs(r, c):

            q = deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            while q:
                curr_r, curr_c = q.popleft()  # Change this to pop() for DFS

                for inc_r, inc_c in directions:
                    new_r, new_c = curr_r + inc_r, curr_c + inc_c

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visit and grid[new_r][new_c] == "1":
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        islands = 0
                    
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1":
                    islands += 1
                    bfs_dfs(r, c) 

        return islands
    
solution_obj = Solution()
print(solution_obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # 1
print(solution_obj.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # 3


from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.res = []

    def canFinish(self, crs: int, pre: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        in_degree = [0] * crs

        for e1, e2 in pre:
            adj_list[e2].append(e1)
            in_degree[e1] += 1

        q = deque()

        for node in range(len(in_degree)):
            if in_degree[node] == 0:
                q.append(node)

        while q:
            
            course_taken = q.popleft()

            crs -= 1 # Decrement the number of courses taken as we are taking a course
            self.res.append(course_taken)


            for dest_edge in adj_list[course_taken]:
                in_degree[dest_edge] -= 1
                if in_degree[dest_edge] == 0:
                    q.append(dest_edge)

        
        if not crs:
            return True

        self.res = []

        return False
    
solution_obj = Solution()
print(solution_obj.canFinish(2, [[1,0]]), solution_obj.res) # True
print(solution_obj.canFinish(2, [[1,0],[0,1]]), solution_obj.res) # False
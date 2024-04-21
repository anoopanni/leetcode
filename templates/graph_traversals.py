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




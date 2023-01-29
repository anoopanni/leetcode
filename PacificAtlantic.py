# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visit_a = set()
        visit_p = set()

        # def dfs(r, c, visit):
        #     q = collections.deque()
        #     q.append((r, c))
        #     visit.add((r, c))
        #     directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
             
        #     while q:
        #         p_row, p_col = q.pop()
                
        #         for each_d in directions:
        #             new_r = p_row + each_d[0]
        #             new_c = p_col + each_d[1]

        #             if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visit and heights[new_r][new_c] >= heights[p_row][p_col]:
        #                 q.append((new_r, new_c))
        #                 visit.add((new_r, new_c))

        # for i in range(COLS):
        #     if heights[0][i] not in visit_p:
        #         dfs(0, i, visit_p)

        # for i in range(ROWS):
        #     if heights[i][0] not in visit_p:
        #         dfs(i, 0, visit_p)

        # for i in range(COLS):
        #     if heights[ROWS-1][i] not in visit_a:
        #         dfs(ROWS-1, i, visit_a)

        # for i in range(ROWS):
        #     if heights[i][COLS-1] not in visit_a:
        #         dfs(i, COLS-1, visit_a)

        # t_res = visit_a.intersection(visit_p)
        # res = [[x[0], x[1]] for x in t_res]

        # return res


        # Solution 2 - Recursive solution :

        def dfs(r, c, visit, prev):
            print(prev)

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or prev > heights[r][c]:
                return 

            visit.add((r, c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        

        for i in range(COLS):
            if heights[0][i] not in visit_p:
                dfs(0, i, visit_p, heights[0][i])

        for i in range(ROWS):
            if heights[i][0] not in visit_p:
                dfs(i, 0, visit_p, heights[i][0])

        for i in range(COLS):
            if heights[ROWS-1][i] not in visit_a:
                dfs(ROWS-1, i, visit_a, heights[ROWS-1][i])

        for i in range(ROWS):
            if heights[i][COLS-1] not in visit_a:
                dfs(i, COLS-1, visit_a, heights[i][COLS-1])

        t_res = visit_a.intersection(visit_p)
        res = [[x[0], x[1]] for x in t_res]

        return res


        
            
                    
                
                

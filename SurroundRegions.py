# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/description/


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or board[r][c] == 'X':
                return
            
            board[r][c] = 'E'
            visit.add((r, c))

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)


        # Change all the border one's from 'O' to 'E'

        for r in range(0, ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visit and (r in {0, ROWS-1} or c in {0, COLS-1}):
                    dfs(r, c)  

        # for i in range(0, COLS):
        #     if board[ROWS-1][i] == 'O' and (ROWS-1, i) not in visit:
        #         dfs(ROWS-1, i)  

        # for i in range(0, ROWS):
        #     if board[i][0] == 'O' and (i, 0) not in visit:
        #         dfs(i, 0) 

        # for i in range(0, ROWS):
        #     if board[i][COLS-1] == 'O' and (i, COLS-1) not in visit:
        #         dfs(i, COLS-1) 
             
            
        # Change all the 'O' to 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        
        # Change all the 'E' to 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'E':
                    board[i][j] = 'O'


        
        

        
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]

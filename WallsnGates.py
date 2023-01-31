# 286. Walls and Gates
# https://leetcode.com/problems/walls-and-gates/description/

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        q = collections.deque()
        seen = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):

                if rooms[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))

        while q:
            dist += 1
            for i in range(len(q)):

                p_r, p_c = q.popleft()
            
                for d in directions:
                    n_r, n_c = p_r + d[0], p_c + d[1]

                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and rooms[n_r][n_c] not in seen and rooms[n_r][n_c] == 2147483647:
                        rooms[n_r][n_c] = dist 
                        seen.add((n_r, n_c))
                        q.append((n_r, n_c))

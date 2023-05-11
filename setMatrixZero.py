# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Solution 1 - Using extra memory O(m+n)

        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        
        # rows = [False] * ROWS
        # cols = [False] * COLS

        # for i in range(ROWS):
        #     for j in range(COLS):

        #         if matrix[i][j] == 0:
        #             rows[i] = True
        #             cols[j] = True

        # for i in range(ROWS):
        #     for j in range(COLS):

        #         if rows[i] or cols[j]:
        #             matrix[i][j] = 0



        # Solution 2 - Using constant memory O(1), shifting the above rows and cols array inside matrix

        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowSave = 1
        
        # Go through each elements in the matrix and set first row and first column to zero.
        for i in range(ROWS):
            for j in range(COLS):
                
                if matrix[i][j] == 0:
                    if i == 0:
                        rowSave = 0
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Go through each element except for first row and first column to set elements to zero.
        for i in range(1, ROWS):
            for j in range(1, COLS):

                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # if matrix[0][0] is zero, set the first column elements to zero
        if matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0

        # if rowSave is zero, set the first row elements to zero
        if rowSave == 0:
            for j in range(COLS):
                matrix[0][j] = 0


        

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
  
  
# Example 2:

  
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

                    

                    
 
                
                    










        

        

        

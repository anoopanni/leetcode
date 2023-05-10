# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Solution 1 - using 4 pointer approach 

        l, r = 0, len(matrix) - 1
        
        while l < r:
            t, b = l, r

            for i in range(r-l):
                
                # save the top left element
                topLeft = matrix[t][l+i]

                # shift bottom left element
                matrix[t][l+i] = matrix[b-i][l]

                # shift bottom right element
                matrix[b-i][l] = matrix[b][r-i]

                # shift top right element
                matrix[b][r-i] = matrix[t+i][r]

                # put back topLeft element
                matrix[t+i][r] = topLeft

            l += 1
            r -= 1


        
        # Solution 2 - Reversing rows and transpose(internchanging rows and columns)

        # rows, cols = len(matrix), len(matrix[0])
        # t, b = 0, rows-1

        # while t < b:
        #   matrix[t], matrix[b] = matrix[b], matrix[t]
        #   t += 1
        #   b -= 1

        # for i in range(rows):
        #     for j in range(i):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
          

        # Solution 3 - Interchanging row elements with column elements (Doesn't work in-place)
        # O(n^2) extra memory 

        # rows, cols = len(matrix), len(matrix[0])
        # n_matrix = [[0 for j in range(cols)] for i in range(rows)]

        # for i in range(rows):
        #     for j in range(cols):
        #         n_matrix[j][cols-i-1] = matrix[i][j]
        
        # matrix = n_matrix
        
            

            
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
  
  
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
  

    


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # l, r = 0, len(matrix[0]) 
        # t, b = 0, len(matrix) 

        # res = []

        # while l < r and t < b:

        #     # Top elements from left to right

        #     for i in range(l, r):
        #         res.append(matrix[t][i])
        #     t += 1

        #     # Right elements from top to bottom

        #     for i in range(t, b):
        #         res.append(matrix[i][r-1])
        #     r -= 1
            

        #     if not (l < r and t < b):
        #         break

        #     # Bottom elements from right to left

        #     for i in range(r-1, l-1, -1):
        #         res.append(matrix[b-1][i])
            
        #     b -= 1
        #     # Left elements from bottom to top

        #     for i in range(b-1, t-1, -1):
        #         res.append(matrix[i][l])

        #     l += 1
            
        # return res



    # Solution 2 - My Version: 

        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) -1 

        res = []

        while l <= r and t <= b:

            # Top elements from left to right

            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            
            # Right elements from top to bottom

            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1

            if not (l <= r and t <= b):
                break

            # Bottom elements from right to left

            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1

            # Left elements from bottom to top

            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1

        return res
        


    # Solution 3 - Modified jump 2 steps version. 


        # l, r = 0, len(matrix[0]) - 1
        # t, b = 0, len(matrix) -1 

        # res = []

        # while l <= r and t <= b:

        #     # Top elements from left to right

        #     for i in range(l, r+1):
        #         res.append(matrix[t][i])
        #     t += 1
            
        #     # Right elements from top to bottom

        #     for i in range(t, b+1):
        #         res.append(matrix[i][r])
        #     r -= 1

        #     if not (l <= r and t <= b):
        #         break

        #     # Bottom elements from right to left

        #     for i in range(r, l-1, -1):
        #         res.append(matrix[b][i])            
        #     b -= 1

        #     # Left elements from bottom to top

        #     for i in range(b, t-1, -1):
        #         res.append(matrix[i][l])
        #     l += 1

        # # Modify one jumps to two jumps

        # res2 = []

        # for i in range(len(res)):
        #     if i % 2 == 0:
        #         res2.append(res[i])

        # return res2


        # Technique to do it without another run through res is to check whether previous for loop has even number of elements traversed, if yes nothing to do, if its was odd, then start the next for loop with one position ahead of where you would have. 
            



# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
  
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]





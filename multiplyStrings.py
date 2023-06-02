# https://leetcode.com/problems/multiply-strings/description/
# 43. Multiply Strings


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # Solution 1 - Brute Force 

        # return str(int(num1) * int(num2))

        # Solution 2 - Kind of brute force, doesn't work efficiently for big integers

        # if num1 == "0" or num2 == "0":
        #     return "0"

        # res = 0

        # num1 = num1[::-1]
        # num2 = num2[::-1]

        # for i in range(len(num1)):
        #     x = 1
        #     for p in range(i):
        #         x *= 10
        #     for j in range(len(num2)):
        #         y = 1
        #         for q in range(j):
        #             y *= 10
                
        #         res += (x * int(num1[i])) * (y * int(num2[j]))

        # return str(res)


        # Solution 3 - efficient way for multiplying large integers
        
        s = set([num1, num2])
        if "0" in s:
            return "0"


        res = [0] * (len(num1) + len(num2))
        res_str = ''

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                mult = int(num1[i]) * int(num2[j])
                res[i+j] += mult
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] = res[i+j] % 10


        beg = True
        for c in res[::-1]:
            if beg and c == 0:
                continue
            beg = False
            res_str += str(c)

        return res_str

       
 # Elementary multiplication example : 
#   i       2 1 0
#  num1     1 2 3
#  num2     4 5 6

    #     7 3 8
    #   6 1 5 *
    # 4 9 2 * *
    # ----------      
    # 5 6 0 8 8
        
       
      
# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
  
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

        
        
        
        

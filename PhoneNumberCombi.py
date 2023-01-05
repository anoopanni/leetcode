# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", 
        "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}     
        res = [] 

        def backTracking(curStr, i):

            if i == len(digits):
                res.append(curStr)
                return
            
            for l in mapping[digits[i]]:
                backTracking(curStr + l, i+1)

        if digits:
            backTracking('',0)

        return res
        

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
        

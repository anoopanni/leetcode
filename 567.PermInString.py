# https://leetcode.com/problems/permutation-in-string/description/
# 567. Permutation in String


from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # O(n*26) = O(n) solution using hashmap comparisions

        if len(s1) > len(s2):
            return False

        freq_s1 = collections.defaultdict(int)
        freq_s2 = collections.defaultdict(int)
        l = 0

        for s in s1:
            freq_s1[s] += 1


        for r in range(len(s2)):
            freq_s2[s2[r]] += 1


            if r - l + 1 == len(s1): 
                if freq_s1 == freq_s2:
                    return True
                else:
                    freq_s2[s2[l]] -= 1
                    if freq_s2[s2[l]] <= 0:
                        del freq_s2[s2[l]]
                    l += 1

        return False



        # More Optimised Solution O(26) + O(n) using matches technique 

        # if len(s1) > len(s2):
        #     return False

        # count1 = [0] * 26
        # count2 = [0] * 26
        # l = 0  

        # for i in range(len(s1)):
        #     count1[ord(s1[i]) - ord('a')] += 1
        #     count2[ord(s2[i]) - ord('a')] += 1


        # matches = 0
        # for i in range(26):
        #     if count1[i] == count2[i]:
        #         matches += 1

        
        # for r in range(len(s1), len(s2)):

        #     if matches == 26:
        #         return True

        #     index = ord(s2[r]) - ord('a')
        #     count2[index] += 1

        #     if count1[index] == count2[index]:
        #         matches += 1
        #     elif count1[index] + 1 == count2[index]:
        #         matches -= 1

        #     index = ord(s2[l]) - ord('a')
        #     count2[index] -= 1

        #     if count1[index] == count2[index]:
        #         matches += 1
        #     elif count1[index] - 1 == count2[index]:
        #         matches -= 1

        #     l += 1

        # return matches == 26
            
            


        # Non-Efficient solution.

        # if len(s1) > len(s2):
        #     return False

        # l, r = 0, len(s1)
        # count1 = Counter(s1)

        # for i in range(len(s2)):

        #     count2 = Counter(s2[l+i:r+i])

        #     if count1 == count2:
        #         return True
            
        # return False





# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
  
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false



            


            

            









                
            









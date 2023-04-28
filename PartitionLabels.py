# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        count_end = {}
        for i in range(len(s)):
            count_end[s[i]] = i
        
        start = 0
        max_e = 0
        res = []
 
        for i in range(len(s)):
            max_e = max(max_e, count_end[s[i]])
            if i == max_e:
                res.append(max_e - start + 1)
                start = max_e + 1
        return res


        # lastIndex = {}

        # for i, c in enumerate(s):
        #     lastIndex[c] = i

        # print(lastIndex)

        # res = []
        # size, end = 0, 0

        # for i, c in enumerate(s):
        #     size += 1
        #     end = max(end, lastIndex[c])
        #     if i == end:
        #         res.append(size)
        #         size = 0

        # return res



            
# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        # @lru_cache(None)
        # def top_down(i):
            
        #     if i == len(s):
        #         return 1

        #     if s[i] == "0":
        #         return 0

        #     res = 0

        #     res += top_down(i+1)

        #     if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and int(s[i+1]) <= 6):
        #         res += top_down(i+2)

        #     return res

        # return top_down(0)


        def bottom_up():
            table = [0] * (len(s)+1)
            table[0] = 1


            if int(s[0]) >= 1:
                table[1] = 1
            else:
                return 0 # No possible ways to decode if it starts from 0


            for i in range(2, len(s)+1):
                if s[i-1] != "0":
                    table[i] += table[i-1]
                
                if (s[i-2] == "2" and ( 6 >= int(s[i-1]) >= 0 )) or s[i-2] == "1":
                    table[i] += table[i-2]

            return table[len(s)]

        return bottom_up()


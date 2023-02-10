# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra's problem

        adjList = {i:[] for i in range(1, n+1)}

        for t in times:
            adjList[t[0]].append([t[2], t[1]])

        visit = set()
        res = 0

        minCost = [(0, k)]

        while minCost:

            cost, p_node = heapq.heappop(minCost)

            if p_node in visit:
                continue

            visit.add(p_node)

            res = cost

            for neig in adjList[p_node]:
                if neig[1] not in visit:
                    heapq.heappush(minCost, (cost+neig[0], neig[1]))


        return res if len(visit) == n else -1




            
        

        
                



                



                



        

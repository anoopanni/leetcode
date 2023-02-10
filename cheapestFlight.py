# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Solution 1 :


        # prices = [float("inf")] * n
        # prices[src] = 0

        # for i in range(k + 1):
        #     tmpPrices = prices.copy()

        #     for s, d, p in flights:  # s=source, d=dest, p=price
        #         if prices[s] == float("inf"):
        #             continue
        #         if prices[s] + p < tmpPrices[d]:
        #             tmpPrices[d] = prices[s] + p
        #     prices = tmpPrices
        # return -1 if prices[dst] == float("inf") else prices[dst]





        # Solution 2 - using BFS and queue


        adjList = {i:[] for i in range(n)}
        distance = [float('inf')] * (n)

        for f in flights:
            adjList[f[0]].append((f[2], f[1]))
        
        q = collections.deque()
        q.append((0, 0, src))

        while q:

            stops, cost, node = q.popleft()

            if stops > k:
               continue

            for neig in adjList[node]:
                if stops <= k and (cost + neig[0] < distance[neig[1]]):
                    distance[neig[1]] = cost + neig[0]
                    q.append(((stops + 1), cost + neig[0], neig[1]))
            
        if distance[dst] == float('inf'):
            return -1

        return distance[dst]

            



# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.



# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.






        

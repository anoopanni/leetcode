# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
# 1584. Min Cost to Connect All Points



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Solution 1 - Prim's algorithm


        # n = len(points)

        # adjList = {i:[] for i in range(n)}

        # for i in range(n):
        #     x1, y1 = points[i]
        #     for j in range(i+1, n):
        #         x2, y2 = points[j]
        #         cost = abs(x1 - x2) + abs(y1 - y2)
        #         adjList[i].append([cost, j])
        #         adjList[j].append([cost, i])


        # visit = set()
        # minCost = [[0, 0]]
        # res = 0

        # # Prim's algorithm - O(n^2 log n)

        # while len(visit) != n:
        #     cost, p = heapq.heappop(minCost)

        #     if p in visit:
        #         continue

        #     res += cost
        #     visit.add(p)

        #     for neig in adjList[p]:
        #         if neig[1] not in visit:
        #             heapq.heappush(minCost, neig)
                
        # return res




        # from collections import defaultdict

  
        # adjM = defaultdict(list)

        # for i in range(len(points)):
        #     x1, y1 = points[i]
            
        #     for j in range(i+1, len(points)):
        #         x2, y2 = points[j]

        #         cost = abs(x2-x1) + abs(y2-y1)
        #         adjM[i].append((cost, j))
        #         adjM[j].append((cost, i))

        

        # visit = set()
        # minCost = [(0, 0)]
        # res = 0

        # import heapq


        # while len(visit) != len(points):
        #     cost, p = heapq.heappop(minCost)

        #     if p in visit:
        #         continue

        #     visit.add(p)
        #     res += cost

        #     for n in adjM[p]:
        #         heapq.heappush(minCost, n)

        # return res



        # Solution 2 - Kruskal's algorithm - Algorithm for MST(minimum spanning tree) 

        edges = []
        n = len(points)
        res = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                edges.append((i, j, abs(x2-x1) + abs(y2-y1)))

        edges = sorted(edges, key=lambda x: x[2])


        parents = list(range(n))
        ranks = [0] * n

        def find(n):
            
            while n != parents[n]:
                n = parents[n]
            return n

        
        def union(e1, e2):
            e1 = find(e1)
            e2 = find(e2)

            if e1 != e2:
                if ranks[e1] >= ranks[e2]:
                    parents[e2] = e1
                    ranks[e1] += 1
                else:
                    parents[e1] = e2
                    ranks[e2] += 1


        for e in edges:
            if find(e[0]) != find(e[1]):
                union(e[0], e[1])
                res += e[2]

        return res



                







        

        

        

































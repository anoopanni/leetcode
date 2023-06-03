# 2013. Detect Squares
# https://leetcode.com/problems/detect-squares/description/


from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point

        for x,y in self.points:
            if abs(qx - x) != abs(qy - y) or (x == qx) and (y == qy):
                continue 
            if (x, qy) in self.points and (qx, y) in self.points:
                res += (self.points[(x, qy)] * self.points[(qx, y)] * self.points[(x, y)])
                
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


# Input

# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]

# Output

# [null, null, null, null, 1, 0, null, 2]

# Explanation
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // return 1. You can choose:
#                                //   - The first, second, and third points
# detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
# detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
# detectSquares.count([11, 10]); // return 2. You can choose:
#                                //   - The first, second, and third points
#                                //   - The first, third, and fourth points

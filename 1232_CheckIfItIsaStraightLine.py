class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]

        if x1 == x2:
            for coordinate in coordinates:
                if coordinate[0] != x1:
                    return False                    
            return True
        else:
            a = (y2 - y1) / (x2 - x1)
            b = y1 - a * x1
            for coordinate in coordinates:
                if (a * coordinate[0] + b) != coordinate[1]:
                    return False
            return True

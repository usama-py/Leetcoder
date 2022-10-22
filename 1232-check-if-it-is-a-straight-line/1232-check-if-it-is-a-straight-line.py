class Solution:
    def slope(self, x1, y1, x2, y2):
        if(x2 - x1 != 0):
            return (float)(y2-y1)/(x2-x1)
        return sys.maxsize * 2 + 1
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        ans = self.slope(coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1])
        for i in range(len(coordinates)-1):
            temp = self.slope(coordinates[i][0],coordinates[i][1],coordinates[i+1][0],coordinates[i+1][1])
            if ans != temp:
                return False
            ans = temp
        return True
        
        
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        check = False
        # if len(grid[0])<=len(grid):
        #     for i in range(len(grid)):
        #         if grid[i][i] != 1:
        #             check = False
        #             break
        #         else:
        #             check = True
        #     if check:
        #         return [-1]*len(grid)
        #     for i in range(len(grid)-1,-1,-1):
        #         if grid[i][i] != -1:
        #             check = False
        #             break
        #         else:
        #             check = True
        #     if check:
        #         return [-1]*len(grid)
        q = 0
        ans = []
        for i in range(len(grid[0])):
            q = i
            for j in range(len(grid)):
                if grid[j][q] == -1 and q == 0:
                    ans.append(-1)
                    break
                elif grid[j][q] == 1 and q == len(grid[j])-1:
                    ans.append(-1)
                    break
                if grid[j][q] == 1 and q <len(grid[j])-1:
                    if grid[j][q+1] == -1:
                        ans.append(-1)
                        break
                elif grid[j][q] == -1 and q > 0:
                    if grid[j][q-1] == 1:
                        ans.append(-1)
                        break
                if grid[j][q] == 1:
                    q += 1
                elif grid[j][q] == -1:
                    q -= 1
                if j == len(grid)-1:
                    ans.append(q)
                    break
        print(ans)
        return ans
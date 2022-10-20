class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # count = len(colors)
        # if count == 1:
        #     return 0
        # c = Counter(colors)
        # for v in c.values():
        #     if v == 1:
        #         count -= 1
        #     elif len(colors) == v:
        #         neededTime.sort()
        #         return sum(neededTime[:len(colors)-1])
        # if count == 0:
        #     return 0
        ans = 0
        for i in range(len(colors)):
            if i <= len(colors)-2 and colors[i] == colors[i+1]:
                print(neededTime[i],neededTime[i+1])
                temp = min(neededTime[i],neededTime[i+1])
                temp2 = max(neededTime[i],neededTime[i+1])
                neededTime[i] = temp
                neededTime[i+1] = temp2
                ans += temp
        return ans
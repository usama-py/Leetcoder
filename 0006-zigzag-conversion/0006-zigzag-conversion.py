class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s = list(s)
        a = []
        ans = ''
        p = 0
        for i in range(numRows):
            a.append([])
        for i in range(len(s)):
            for j in range(numRows):
                a[j].append(s[p])
                p += 1
                if p >= len(s):
                    break
            if p >= len(s):
                break
            for k in range(numRows-2,0,-1):
                a[k].append(s[p])
                p += 1
                if p >= len(s):
                    break
            if p >= len(s):
                break
        for ele in a:
            for ele1 in ele:
                ans += ele1
        return ans
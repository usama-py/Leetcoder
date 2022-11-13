class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        a = s.split(" ")
        a.reverse()
        ans = ''
        for i in range(len(a)):
            if a[i] != '':
                ans += a[i]
                if i < len(a) - 1:
                    ans += ' '
        return ans
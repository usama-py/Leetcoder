class Solution:
    def reverseVowels(self, s: str) -> str:
        p = len(s)-1
        a = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        b = set(a)
        q = 0
        for i in range(len(s)):
            
            if s[p] not in b:
                p -= 1
            if s[q] not in b:
                q += 1
            if s[p] in b and s[q] in b:
                temp = s[p]
                s[p] = s[q]
                s[q] = temp
                p -= 1
                q += 1
            if p<=q:
                break
        return ''.join(s)
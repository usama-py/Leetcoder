class Solution:
    def reverseString(self, s: List[str]) -> None:
        p = len(s)-1
        i = 0
        for ele in s:
            s[i] = s[p]
            s[p] = ele
            i += 1
            p -= 1
            if i == len(s)//2:
                break
        
        
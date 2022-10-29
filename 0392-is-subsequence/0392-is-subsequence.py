class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        j = 0
        check = 0
        for ele in s:
            for i in range(j,len(t)):
                if t[i] == ele:
                    j+=1
                    check += 1
                    break
                j+=1
        return check == len(s)
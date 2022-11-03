class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        p = len(x)-1
        
        for i in range(len(x)//2):
            print(x[i],x[p])
            if x[i] != x[p]:
                return False
            p -= 1
        return True
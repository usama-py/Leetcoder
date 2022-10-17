class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        if n == 0:
            return 0
        t1 = 0
        t2 = 1
        t3 = 1
        a = 0
        for i in range(n-2):
            a = t1+t2+t3
            t1 = t2
            t2 = t3
            t3 = a
        return a
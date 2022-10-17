class Solution:
    def fib(self, n: int) -> int:
        temp = 2.23606797749979
        a = (((1+temp)/2)**n)
        b = (((1-temp)/2)**n)
        return ((a - b)/ temp).__round__()
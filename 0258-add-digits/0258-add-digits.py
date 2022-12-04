class Solution:
    def add(self,num):
        if num < 10:
            return num
        else:
            num = self.add(num//10)+(num%10)
        num = self.add(num//10)+(num%10)
        return num
            
        
        
    def addDigits(self, num: int) -> int:
        return self.add(num)
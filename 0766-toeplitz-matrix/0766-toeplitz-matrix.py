class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            ele = matrix[i]
            ele2 = matrix[i+1]
            if ele[:len(ele)-1] != ele2[1:]:
                return False
        return True
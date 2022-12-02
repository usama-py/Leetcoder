class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            first = i
            last = n-i-1
            for j in range(first,last):
                top = matrix[i][j]
                matrix[i][j] = matrix[-j-1][i]
                matrix[-j-1][i] = matrix[-i-1][-j-1]
                matrix[-i-1][-j-1] = matrix[j][-i-1]
                matrix[j][-i-1] = top
        
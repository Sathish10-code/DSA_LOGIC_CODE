class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(n):
            st = 0
            end = n-1
            while st<end:
                temp = matrix[i][st]
                matrix[i][st] = matrix[i][end]
                matrix[i][end] = temp
                st+=1
                end-=1
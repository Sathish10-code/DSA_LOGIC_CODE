class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n==1 or m==1:
            return 1
        grid = [[1]*m for i in range(n)]

        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]
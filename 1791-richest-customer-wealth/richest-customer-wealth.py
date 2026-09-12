class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row = len(accounts)
        col = len(accounts[0])
        maxi=0
        for i in range(row):
            cur = 0
            for j in range(col):
                cur+=accounts[i][j]
            maxi =  max(cur,maxi)
        
        return maxi
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in range(len(accounts)):
            cur = sum(accounts[i])
            maxi =  max(cur,maxi)
        
        return maxi
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p,max_p = prices[0],0
        l,r=0,len(prices)-1
        while l<=r:
            cur = prices[l]-min_p
            min_p = min(prices[l],min_p)
            max_p = max(cur,max_p)
            l+=1
        
        return max_p

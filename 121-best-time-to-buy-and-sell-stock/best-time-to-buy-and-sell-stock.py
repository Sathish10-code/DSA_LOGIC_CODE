class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        mini = prices[0]
        maxi = prices[0]
        for i in prices:
            if i < mini:
                prof = max(maxi-mini,prof)
                mini=i
                maxi=i
            if i>maxi:
                maxi=i
        return max(maxi-mini, prof)
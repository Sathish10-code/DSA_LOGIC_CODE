class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        mini = prices[0]
        maxi = prices[0]
        for i in prices:
            if i <mini:
                profit = max(maxi-mini, profit)
                mini=i
                maxi =i
            elif i>maxi:
                maxi=i
        return max(maxi-mini,profit)

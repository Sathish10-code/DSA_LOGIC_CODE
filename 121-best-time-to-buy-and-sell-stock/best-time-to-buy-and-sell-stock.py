class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro =0
        maxi = mini = prices[0]
        for i in prices[1:]:
            if i < mini:
                pro = max(pro, maxi-mini)
                mini = i
                maxi = i
            if i > maxi:
                maxi = i
        return max(pro , maxi-mini)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        tot = 0
        for pre in prices:
            if pre > prev:
                tot += pre - prev
            prev = pre
        return tot 
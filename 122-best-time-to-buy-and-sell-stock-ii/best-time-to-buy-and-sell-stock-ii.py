class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro =0 
        mini = prices[0]
        for n in prices[1:]:
            if mini < n:
                ans = n-mini
                pro +=ans
                mini = n
            if mini > n:
                mini =n
        return pro
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=prices[0]
        mini=prices[0]
        pro=0
        for i in prices[1:]:
            if i < mini:
                pro= max(maxi-mini,pro)
                mini=i
                maxi=i
            if i> maxi:
                maxi=i
        return max(pro,maxi-mini)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxi = float('-inf') 
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            if curr>maxi:
                maxi=curr
        return maxi
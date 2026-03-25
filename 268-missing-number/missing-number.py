class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        add = n*(n+1) //2
        return add - sum(nums)
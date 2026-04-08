class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        tot=0
        minsize=float('inf')
        for r in range(len(nums)):
            tot += nums[r]
            while tot>=target:
                minsize = min(minsize,r-l+1)
                tot-=nums[l]
                l+=1
        return 0 if minsize ==float('inf')  else minsize
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_end = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=final_end:
                final_end=i
        if not final_end:
            return True
        else:
            return False
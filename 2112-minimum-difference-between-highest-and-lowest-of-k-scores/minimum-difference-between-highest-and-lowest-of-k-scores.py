class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        
        nums.sort()
        min_dif = float('inf')
        for i in range(len(nums)-k+1):
            cur_dif = nums[i+k-1]-nums[i]
            min_dif = min(min_dif,cur_dif)
        
        return min_dif
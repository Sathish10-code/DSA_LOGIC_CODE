class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reach , jump , end = 0,0,0
        for i in range(n-1):
            max_reach = max(max_reach,i+nums[i])
            if i == end:
                jump+=1
                end = max_reach
        return jump
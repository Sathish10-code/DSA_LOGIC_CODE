class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_map = {0:-1}
        prefix_sum = 0
        max_sum  = 0

        for i,num in enumerate(nums):
            prefix_sum +=1 if num==1 else -1
            if prefix_sum in sum_map:
                max_sum = max(max_sum , (i - sum_map[prefix_sum]))
            else:
                sum_map[prefix_sum] = i
        return max_sum
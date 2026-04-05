class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==0: return []
        
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        # print(nums)
        return nums
        
        
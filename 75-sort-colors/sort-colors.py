class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind =0
        for i in range(0,len(nums)):
            if nums[i]==0:
                nums[i],nums[ind]=nums[ind],nums[i]
                ind+=1
        for i in range(ind,len(nums)):
            if nums[i]==1:
                nums[i],nums[ind]=nums[ind],nums[i]
                ind+=1
        
        return nums
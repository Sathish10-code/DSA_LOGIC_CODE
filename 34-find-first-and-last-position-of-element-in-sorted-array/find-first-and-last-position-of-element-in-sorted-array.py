class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_pos(nums):
            left,right =0,len(nums)-1
            index =-1
            while left <=right:
                mid = (left+right)//2
                if nums[mid]<target:
                    left = left+1
                else:
                    right -=1
                if nums[mid]==target:
                    index= mid
            return index
        
        def last_pos(nums):
            left,right =0,len(nums)-1
            index=-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]>target:
                    right-=1
                else:
                    left +=1
                if nums[mid]==target:
                    index=mid
            return index
        
        fir = first_pos(nums)
        las = last_pos(nums)
        return [fir,las]

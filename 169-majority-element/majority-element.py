class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority = 0
        # count=0
        # for n in nums:
        #     if count==0:
        #         majority = n
        #         count=1
        #     elif majority == n:
        #         count+=1
        #     else:
        #         count-=1
        # return majority
        nums.sort()
        first =0
        last = len(nums)-1
        mid = len(nums)//2
        while(first<=last):
            if nums[first]==nums[mid] or nums[last]==nums[mid]:
                return nums[mid]
            else:
                first+=1
                last-=1
                

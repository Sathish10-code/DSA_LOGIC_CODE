class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}

        for i in range(len(nums)):
            n=nums[i]
            dif = target - n
            if dif in prev:
                return [prev[dif],i]
            prev[n]=i
        
        return [-1,-1]
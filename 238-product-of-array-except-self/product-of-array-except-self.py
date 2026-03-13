class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre =1
        post = 1
        n=len(nums)
        res =[1]*n
        for i in range(0,n,1):
            res[i] = res[i]*pre
            pre*=nums[i]
        for i in range(n-1,-1,-1):
            res[i]= res[i]*post
            post*=nums[i]
        return res
        
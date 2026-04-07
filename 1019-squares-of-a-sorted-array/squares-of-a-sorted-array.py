class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==0: return []
        
        res =[0]*len(nums)

        l,r=0,len(nums)-1
        index = len(nums)-1
        while(l<=r):
            lft = nums[l]*nums[l] 
            rgt = nums[r]*nums[r]
            if lft>=rgt:
                res[index]=lft
                l+=1
            else:
                res[index]=rgt
                r-=1
            index-=1
        return res        
        
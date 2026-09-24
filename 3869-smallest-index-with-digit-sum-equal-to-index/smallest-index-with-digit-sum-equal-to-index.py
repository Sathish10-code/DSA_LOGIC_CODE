class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res=-1
        for i in range(len(nums)):
            if nums[i]>=10:
                add=0
                seq=nums[i]
                while seq>0:
                    add+=seq%10
                    seq=seq//10
                if add == i and res ==-1:
                    res = i
                elif add==i:
                    res = min(res,i)
            elif nums[i]==i and res ==-1:
                res = i
            elif nums[i]==i:
                res = min(i,res)
        return res 
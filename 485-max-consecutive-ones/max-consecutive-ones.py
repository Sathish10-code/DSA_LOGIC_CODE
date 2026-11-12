class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count =0
        maxi =0
        for x in nums:
            if x ==1:
                count+=1
                maxi = max(count,maxi)
            else:
                count=0
        return maxi
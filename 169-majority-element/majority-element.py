class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count ={}
        for n in nums:
            count[n] = count.get(n,0)+1
        for n,f in count.items():
            if f > len(nums)//2:
                return n
            

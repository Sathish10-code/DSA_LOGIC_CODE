class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = []
        counts={}

        for i in nums:
            counts[i] = counts.get(i,0)+1
        
        for i in counts:
            if counts[i]>1:
                l.append(i)
        return l
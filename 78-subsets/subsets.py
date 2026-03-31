class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            temp=[]
            for subset in res:
                new_subset = subset+[num]
                temp.append(new_subset)
            res+=temp
        return res

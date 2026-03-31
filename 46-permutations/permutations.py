class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_res=[]
        def backtracking(current,remainder):
            if(len(remainder)==0):
                final_res.append(current)
                return
            for i in range(len(remainder)):
                new_cur = current + [remainder[i]]
                new_rem = remainder[:i]+remainder[i+1:]
                backtracking(new_cur,new_rem)
        backtracking([],nums)

        return final_res
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # rank_map={}
        # rank=1
        # for num in sorted(arr):
        #     if num not in rank_map:
        #         rank_map[num]=rank
        #         rank+=1
        # return [rank_map[num] for num in arr]
        sorted_uni_arr = sorted(list(set(arr)))
        rank_map = {val:i+1 for i,val in enumerate(sorted_uni_arr)}
        return [rank_map[num] for num in arr]
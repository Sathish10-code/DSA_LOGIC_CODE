class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        dic = dict(sorted(dic.items(),key= lambda x:x[1],reverse=True ))
        new_dic = dict(islice(dic.items(),k))
        res = list(new_dic.keys())
        # print(res)
        return res
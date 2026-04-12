class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        bucket = [0]*(n+1)
        c = Counter(nums)
        for num,freq in c.items():
            if bucket[freq]==0:
                bucket[freq]=[num]
            else:
                bucket[freq].append(num)
        res =[]
        for freq in range(n,-1,-1):
            if bucket[freq]!=0:
                res.extend(bucket[freq])
            if len(res)==k:
                break
        return res
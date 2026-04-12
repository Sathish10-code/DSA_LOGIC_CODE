class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        c = Counter(nums)
        for i,j in c.items():
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
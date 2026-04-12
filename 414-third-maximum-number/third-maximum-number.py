class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist = set(nums)
        if len(dist)<3:
            return max(nums)
        if len(dist)==3:
            return min(nums)
        min_heap =[]
        for n in dist:
            heapq.heappush(min_heap,n)
            if len(min_heap)>3:
                heapq.heappop(min_heap)
        return min_heap[0]
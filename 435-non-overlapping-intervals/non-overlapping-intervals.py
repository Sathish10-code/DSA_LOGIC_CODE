class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        erase,end =0,-float('inf')

        for interval in intervals:
            if interval[0]<end:
                erase+=1
            else:
                end = interval[1]
        return erase
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])

        result=[intervals[0]]
        for start,end in intervals[1:]:
            prev_interval = result[-1]
            if start <=prev_interval[1]:
                result[-1][1] = max(end,prev_interval[1])
            else:
                result.append([start,end])
        return result
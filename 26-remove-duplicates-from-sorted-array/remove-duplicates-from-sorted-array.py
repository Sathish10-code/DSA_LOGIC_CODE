class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        unique_ele = sorted(list(set(nums)))
        nums[:len(unique_ele)] = unique_ele
        return len(unique_ele)

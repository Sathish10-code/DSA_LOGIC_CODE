class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        list_order = sorted(list(set(nums)))
        nums[:len(list_order)]=list_order
        return len(list_order)

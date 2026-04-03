from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        comman = Counter(nums1) & Counter(nums2)
        print(comman)
        return list(comman.elements())
        
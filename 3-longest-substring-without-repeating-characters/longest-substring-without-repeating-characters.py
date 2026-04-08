class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        l=0
        store =[]
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            if s[r] not in store:
                store.append(s[r])
                count = max(count,r-l+1)
        return count
            
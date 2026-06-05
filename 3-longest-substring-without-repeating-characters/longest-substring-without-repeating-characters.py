class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch=set()
        count=0
        left=0
        for i in range(len(s)):
            while s[i] in ch:
                ch.remove(s[left])
                left+=1
            ch.add(s[i])
            count = max(count,i-left+1)
        return count
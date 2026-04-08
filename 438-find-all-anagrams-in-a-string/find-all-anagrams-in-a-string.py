class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        p = ''.join(sorted(p))
        for i in range(len(s)-len(p)+1):
            ana = s[i:i+len(p)]
            ana = ''.join(sorted(ana))
            if ana == p:
                res.append(i)
        return res
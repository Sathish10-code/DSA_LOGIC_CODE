class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count=0
        i,j=0,0
        if len(s)==0: return True
        if len(s)>len(t): return False
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        
        return len(s)==count
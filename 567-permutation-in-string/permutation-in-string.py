class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m=len(s1),len(s2)
        if n>m:
            return False
        need =[0]*26
        window = [0]*26
        for i in range(n):
            need[ord(s1[i])-ord('a')]+=1
        for j in range(n):
            window[ord(s2[j])-ord('a')]+=1
            if need==window:
                return True
        
        for k in range(n,m):
            window[ord(s2[k])-ord('a')]+=1
            window[ord(s2[k-n])-ord('a')]-=1
            if window == need:
                return True
        return False


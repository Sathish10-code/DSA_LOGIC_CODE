class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        test = "".join(sorted(s1))
        for i in range(len(s2)-len(s1)+1):
            temp = s2[i:i+len(s1)]
            new_temp = "".join(sorted(temp))
            if new_temp == test:
                return True
        
        return False
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s)<10:
            return []

        seen = set()
        repeat = set()
        for i in range(len(s)-9):
            w = s[i:i+10]
            if w in seen:
                repeat.add(w)
            else:
                seen.add(w)
        return list(repeat)

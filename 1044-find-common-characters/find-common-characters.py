from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counts = Counter(words[0])
        for i in range(1,len(words)):
            com = Counter(words[i])
            common_counts = common_counts & com
        
        return list(common_counts.elements())

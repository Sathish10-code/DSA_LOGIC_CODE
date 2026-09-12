class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w = Counter(words)
        return sorted(w, key = lambda x:(-w[x],x))[:k]
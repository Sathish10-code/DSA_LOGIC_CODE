class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d={}
        normalized_word = re.sub(r'[^a-z]',' ',paragraph.lower())
        words = normalized_word.split()
        for i in words:
            if i not in d:
                d[i]=0
            d[i]+=1
        top_freq = dict(sorted(d.items(), key=lambda item:item[1],reverse=True))
        print(top_freq)
        for i in top_freq:
            if i not in banned:
                return i
        
class Solution:
    def secondHighest(self, s: str) -> int:
        first,second=-1,-1
        for ch in s:
            if ch.isdigit():
                c=int(ch)
                if c>first:
                    second,first=first,c
                if second <c<first:
                    second =c
        return second
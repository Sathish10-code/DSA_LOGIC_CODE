class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for ch in zip(*strs):
            # print(set(ch))
            if(len(set(ch))==1):
                # print(ch[0])
                res+=ch[0]
            else:
                break
        return res
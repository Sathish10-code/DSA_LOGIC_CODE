class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        # for word in strs:
        #     count=[0]*26
        #     for letter in word:
        #         ch = ord(letter) - ord('a')
        #         count[ch]+=1
        #     seen[tuple(count)].append(word)
        # return list(seen.values())
        for word in strs:
            w = "".join(sorted(word))
            seen[w].append(word)
        return list(seen.values())
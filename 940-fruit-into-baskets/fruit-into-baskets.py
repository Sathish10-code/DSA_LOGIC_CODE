class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        maxfruits=0
        baskets = defaultdict(int)
        for r in range(len(fruits)):
            if fruits[r] not in baskets:
                while len(baskets) ==2:
                    baskets[fruits[l]]-=1
                    if baskets[fruits[l]]==0:
                        baskets.pop(fruits[l])
                    l+=1
            baskets[fruits[r]]+=1
            maxfruits = max(maxfruits,r-l+1)
        return maxfruits
            
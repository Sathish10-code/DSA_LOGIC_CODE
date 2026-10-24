class Solution:
    def countBits(self, n: int) -> list[int]:
        li = [0]
        for i in range(1,n+1):
            count=0
            while i>0:
                if i%2==1:
                    count+=1
                i//=2
            li.append(count)
        return li

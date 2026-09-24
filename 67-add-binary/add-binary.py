class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = int(a,2)
        n = int(b,2)

        add = m+n
        arr=[]
        if add==0:
            return "0"
        while add>0:
            rem = add%2
            add //=2
            arr.append(str(rem))
        
        return "".join(reversed(arr))
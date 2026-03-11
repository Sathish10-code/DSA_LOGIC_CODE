class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = str(format(n,'b'))
        bi=''
        for i in b:
            if i=='1':
                bi+='0'
            else:
                bi+='1'
        return int(bi,2)
        

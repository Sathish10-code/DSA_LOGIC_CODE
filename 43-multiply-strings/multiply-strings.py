class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                mul = (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                p1,p2 = i+j , i+j+1

                tot = mul + res[p2]

                res[p1] += tot//10
                res[p2] = tot%10

        res_str =[]
        for dig in res:
            if not (len(res_str)==0 and dig==0):
                res_str.append(chr(ord('0')+dig))
        return "".join(res_str)
        

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st=[]
        operators =['+','-','/','*']
        for item in tokens:
            if item not in operators:
                st.append(item)
            else:
                sec = int(st.pop())
                fir = int(st.pop())
                if item =='+':
                    st.append(fir+sec)
                elif item=='-':
                    st.append(fir-sec)
                elif item =='*':
                    st.append(fir*sec)
                else:
                    st.append(fir/sec)
        return int(st[-1])
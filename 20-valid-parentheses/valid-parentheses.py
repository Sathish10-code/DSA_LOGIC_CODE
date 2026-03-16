class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        l=0
        r=len(s)

        while l<r:
            ch = s[l]
            if  ch=='(' or ch=='[' or ch=='{':
                st.append(ch)
            elif not st and (ch==')' or ch=='}' or ch==']'):
                return False
            elif  ch==')':
                if st[-1]=='(':
                    st.pop()
                else:
                    return False
            elif ch==']':
                if st[-1]=='[':
                    st.pop()
                else:
                    return False
            elif ch=='}':
                if st[-1]=='{':
                    st.pop()
                else:
                    return False
            
            l+=1    
        
        return not st
            
            
        
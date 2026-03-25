class Solution {
    public int compress(char[] chars) {
        String s ="";
        int count=0;
        char ptr = chars[0];

        for(char ch:chars){
            if(ptr == ch){
                count++;
            }
            else{
                s+= ptr+(count>1?""+count:"");
                count=1;
                ptr=ch;
            }
        }
        s+=ptr+(count>1?""+count:"");
        for(int i=0;i<s.length();i++){
            chars[i] = s.charAt(i);
        }
        return s.length();
    }
}
class Solution {
    public int secondHighest(String s) {
        int first =-1;
        int second = -1;

        for(char ch:s.toCharArray()){
            if(Character.isDigit(ch)){
                int val = ch-'0';
                if (val>first){
                    second=first;
                    first = val;
                }
                else if (val>=second && val!=first){
                    second = val;
                }
            }
        }
        return second;
    }
}
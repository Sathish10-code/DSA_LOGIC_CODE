class Solution {
    public int binaryGap(int n) {
        String bin = Integer.toBinaryString(n);
        int pos=-1,max=0;

        for(int i=0;i<bin.length();i++){
            if(bin.charAt(i)=='1'){
                if(pos!=-1){
                    max= Math.max(max,i-pos);
                }
                pos=i;
            }
       
        }
        return max; 
    }
}
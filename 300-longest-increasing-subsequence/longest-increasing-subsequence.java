class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] talls = new int[nums.length];
        int size =0 ;
        for(int n:nums){
            int i=0, j=size;
            while(i!=j){
                int mid = (i+j)/2;
                if(talls[mid]<n){
                    i=mid+1;
                }
                else{
                    j=mid;
                }
            }

            talls[i]=n;
            if(i==size) size++;
        }
        return size;
    }
}
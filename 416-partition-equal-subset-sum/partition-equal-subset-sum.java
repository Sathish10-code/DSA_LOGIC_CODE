class Solution {
    public boolean canPartition(int[] nums) {
        int sum=0;
        for(int n:nums){
            sum+=n;
        }
        if(sum%2!=0){ return false;}
        sum=sum/2;

        boolean[] dp = new boolean[sum+1];
        dp[0]=true;

        for(int n:nums){
            for(int j=sum;j>=n;j--){
                dp[j]= dp[j] | dp[j-n];
            }
        }

        return dp[sum];
    }
}
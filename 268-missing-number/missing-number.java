class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = n*(n+1) /2;
        for(int aa:nums){
            sum = sum-aa;
        }
        return sum;
    }
}
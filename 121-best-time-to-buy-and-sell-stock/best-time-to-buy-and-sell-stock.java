class Solution {
    public int maxProfit(int[] prices) {
        int bal=0;
        int i=1,j=prices.length-1;
        int min=prices[0],max=0;
        
        while(i<=j){
            int cur = prices[i]-min;
            max = Math.max(max,cur);
            min = Math.min(min,prices[i]);
            i++;    
        }
        return max;
    }
}
class Solution {
    public int search(int[] nums, int target) {
        if(nums.length==0){
            return -1;
        }
        if(nums.length==1  && nums[0]==target){
            return 0;
        }
        int leftptr = 0;
        int rightptr = nums.length-1;
        while(leftptr <=rightptr){
            int mid = leftptr+ ((rightptr-leftptr)/2);
            if(nums[mid]==target){
                return mid;
            }
            if (nums[leftptr]<=nums[mid]){
                if(nums[leftptr]<=target && target<nums[mid]){
                    rightptr=mid-1;
                }
                else{
                    leftptr=mid+1;
                }
            }
            else{
                if(nums[mid]<target && target <=nums[rightptr]){
                    leftptr = mid+1;
                }
                else{
                    rightptr= mid-1;
                }
            }
        }
        return -1;
    }
}
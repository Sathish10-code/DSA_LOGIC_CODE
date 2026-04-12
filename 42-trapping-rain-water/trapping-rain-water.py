class Solution:
    def trap(self, height: List[int]) -> int:
        left =[0]*len(height)
        right = [0]*len(height)

        max_so_far_left=height[0]

        for i in range(len(height)):
            if height[i]>max_so_far_left:
                max_so_far_left = height[i]
                left[i]=max_so_far_left
            else:
                left[i]=max_so_far_left
        max_so_far_right = height[-1]
        for i in range(len(height)-1,-1,-1):
            if height[i]>max_so_far_right:
                max_so_far_right = height[i]
                right[i]=max_so_far_right
            else:
                right[i]=max_so_far_right
        
        tot =0
        for i in range(len(height)):
            tot = tot +min(left[i],right[i])-height[i]
        
        return tot
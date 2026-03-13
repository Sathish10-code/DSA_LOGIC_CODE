class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxHeight = max(height)
        maxarea=0
        while l<r:

            width =r-l

            if maxHeight*width <=maxarea:
                break
            
            if(height[l]<=height[r]):
                area = height[l]*width
                l+=1
            
            elif(height[l]>height[r]):
                area = height[r]*width
                r-=1

            if area>maxarea:
                maxarea=area
            
        return maxarea
        
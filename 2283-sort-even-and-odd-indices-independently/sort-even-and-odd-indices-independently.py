class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        i,j,k=0,0,0
        while i<len(even) and j<len(odd):
            nums[k]=even[i]
            k+=1
            nums[k]=odd[j]
            k+=1
            i+=1
            j+=1
        
        if i<len(even):
            nums[k]=even[i]
            k+=1
            i+=1
        
        return nums
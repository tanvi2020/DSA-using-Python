class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dip=-1
        n=len(nums)
        # Find the prefix match ,traverse from right to left
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                dip=i # Store the index of the first break point
                break
        if dip==-1:
            nums.reverse()
            return
        # FInd the  element larger than dip but not the largest among all
        for i in range(n-1,dip,-1):
            if nums[i]>nums[dip]:
                nums[i],nums[dip]=nums[dip],nums[i]
                break 
        # Reverse Remaining elements from dip+1 to the end
        start=dip+1
        end=n-1
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        return nums

        

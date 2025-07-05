class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Store the last index of nums1 first
        last=m+n-1
        i=m-1
        j=n-1
        # Start Merging

        while j>=0:
            if i>=0 and nums1[i]>nums2[j]: # if nums1 non zero value > nums2 value at n
                nums1[last]=nums1[i] # Replace last index with nums1 value
                i-=1

            else : # If nums1[m]<nums2[n]
                nums1[last]=nums2[j] # Replace  last index with nums2 value at n
                j-=1
            last-=1

        
            


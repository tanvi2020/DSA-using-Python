class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset=set(nums)
        if len(numset)==len(nums):
            return False  # No duplicates
        else:
            return True # Duplicates exist 



    

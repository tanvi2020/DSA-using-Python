class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        position=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[position]=nums[i]
                position+=1
        return position
        
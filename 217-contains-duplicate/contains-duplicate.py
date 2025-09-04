class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for n in nums:
            if n in dict:
                dict[n]+=1
            else:
                dict[n]=1

            if dict[n]>1:
                return True
        
        return False
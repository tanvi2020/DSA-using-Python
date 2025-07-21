class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for n in nums:
            if n in dict:
                dict[n]+=1
            else:
                dict[n]=1
        for key,value in dict.items():
            if value==1:
                return key
        
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer=[]
        i=0
        while i<len(nums):
            start=nums[i]
            while i+1<len(nums) and nums[i+1]-nums[i]==1:
                i+=1
            end=nums[i]
            if start==end: # Only one number
                answer.append(str(start))
            else:
                answer.append(f"{start}->{end}")
            i+=1
        return answer
        
            


        
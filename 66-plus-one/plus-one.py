class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]>=9:
                digits[i]=0
                i-=1
            else:
                digits[i]+=1
                return digits
        # If all 9's turn into 0's , like for example 999+1 = 1000 we need a 1 at the start
        return [1]+digits
        
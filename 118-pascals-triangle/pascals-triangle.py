class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]

        # Else claculate the previous rows using recurssion
        prevRow=self.generate(numRows-1)
        
        # Build a new row
        newRow=[1]*numRows

        # Fill the ith middle values of new row with sum of prevRow [i]th element + prevRow [i-1]th element
        for i in range(1,numRows-1):
            newRow[i]=prevRow[-1][i]+prevRow[-1][i-1]
            
        # Append the new row into the prevRow list and return the PrevRow list as answer
        prevRow.append(newRow)
        return prevRow
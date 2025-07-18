class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def NCR(n,r):
            res=1
            for i in range(0,r):
                res=res*(n-i)
                res=res//(i+1)
            return res
        row=[]
        for colIndex in range(rowIndex+1):
            row.append((NCR(rowIndex,colIndex)))

        return row
        
                
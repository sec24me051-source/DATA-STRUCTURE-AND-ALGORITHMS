class Solution:
    def searchMatrix(self, m: list[list[int]], target: int) -> bool:
        col=len(m)
        row=len(m[0])
        l=0
        r=(col*row)-1
        while(l<=r):
            mid=(r+l)//2
           
            ro=mid // row
            c=mid % row
            if(m[ro][c]==target):
                return True
            elif(m[ro][c]>target):
                r=mid-1
            else:
                l=mid+1
        else:
            return False
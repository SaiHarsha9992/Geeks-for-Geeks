
from typing import List


class Solution:
    def findClosest(self, n : int, target : int, arr : List[int]) -> int:
        # code here
        val=arr[0]
        mindiff=abs(val-target)
        
        for i in arr:
            diff=abs(i-target)
            
            if diff<mindiff or (diff==mindiff  and i>val):
                val=i
                mindiff=diff
                
        return val
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends
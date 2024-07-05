class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        l = 0
        h = len(A)-1
        mid = 0
        ind = -1
        while(l<=h):
            mid = (l+h)//2
            if A[mid]==X:
                return mid
            elif A[mid]<=X:
                ind = mid
                l = mid+1
            else:
                h = mid-1
        return ind
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
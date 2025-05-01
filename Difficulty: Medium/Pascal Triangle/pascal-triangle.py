#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self, n):
	    # code here
	    tri=[]
        for r in range(n):
            row=[1]*(r+1)
            for c in range(1,r):
                row[c]=tri[r-1][c-1]+tri[r-1][c]
            tri.append(row)
        return tri[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def sieveOfEratosthenes(self, n):
    	#code here 
    	a=[0]*(n+1)
    	a[0]=a[1]=1
    	for i in range(2, int(n**0.5)+1, 1):
    	    if (a[i] == 0):
    	        for j in range(i+i, n+1, i):
    	            a[j]=1
    	
    	return [i for i in range(n+1) if a[i]==0]  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")
# } Driver Code Ends
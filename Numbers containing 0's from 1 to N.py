#User function Template for python3

class Solution:
	def CountNo(self, N):
		# Code here
		c = 0
        for i in range(1,N+1):
            if '0' in str(i):
                c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.CountNo(n)
		print(ans)
# } Driver Code Ends

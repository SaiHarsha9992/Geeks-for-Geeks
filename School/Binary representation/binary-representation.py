#User function Template for python3
class Solution:
	def getBinaryRep(self, n):
		# code here
		return bin(n).replace("0b","0"*(32-len(bin(n))))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.getBinaryRep(n)
		print(ans)

# } Driver Code Ends
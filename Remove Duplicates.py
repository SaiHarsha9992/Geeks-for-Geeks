#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		s = ''
		for i in S:
		    if i not in s:
		        s+=i
		return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends

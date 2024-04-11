# User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
		# code here
		count=0
        s=set(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                sum =arr[i]+arr[j]
                if sum in s:
                    count+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends
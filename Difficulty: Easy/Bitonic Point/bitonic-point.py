#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		for i in range(1,len(arr)-1):
            if arr[i]>arr[i+1] and arr[i] > arr[i-1]:
                return arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends
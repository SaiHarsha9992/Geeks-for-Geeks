class Solution:
    def getXor(self, nums, a, b):
        ans = 0
        for i in range(a, b+1):
            ans = ans ^ nums[i]
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n, a, b = map(int, input().strip().split())
    	nums = list(map(int, input().strip().split()))
    	if(a > b):
    	    a, b = b, a
    	obj = Solution()
    	ans = obj.getXor(nums, a, b)
    	print(ans)
# } Driver Code Ends

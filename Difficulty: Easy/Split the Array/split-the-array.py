#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		#Complete the function
        ans=0
        for i in arr:
            ans^=i
        if ans==0:
            for i in range(len(arr)-1):
                if len(arr)%2==0:
                    return pow(2,len(arr)-1)-1
                return len(arr)
        return 0


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends
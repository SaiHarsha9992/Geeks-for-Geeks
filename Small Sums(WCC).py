#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3

class Solution:
    #Function to find the smallSum of the given array
    def smallSum(self, arr, K):
        #Write your code here
        mod = 10**9+7
        sum = 0
        for i in range(0,len(arr)):
            if arr[i]>arr[i-1]:
                sum += arr[i-1]
            else:
                sum += arr[i-1]%K
        return sum%mod

#{ 
 # Driver Code Starts.

        
if __name__=='__main__':
    test = int(input())
    for _ in range(test):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        obj = Solution()
        answer = obj.smallSum(arr, K)
        print(answer)
# } Driver Code Ends

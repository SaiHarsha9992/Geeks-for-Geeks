#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        r=0
        for i in range(n):
            r^=arr[i]
        return r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
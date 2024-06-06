#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        cnt = 0;
        m = {}
        for i in range(n):
            b= k - arr[i]
            if b in m:
                cnt+=m[b]
            m[arr[i]] = m.get(arr[i], 0) + 1
            
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
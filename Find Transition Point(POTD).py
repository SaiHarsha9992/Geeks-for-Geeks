class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        if arr[n-1] == 0:
            return -1
        flag = True
        for i in range(0,n):
            if arr[i] == 1:
                return i
        return -1
            
            


#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends

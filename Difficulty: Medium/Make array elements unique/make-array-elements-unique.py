#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        n=len(arr)
        ans=0
        sumi=0
        for i in range(1,n):
            before=arr[i]
            if arr[i-1]>=arr[i]:
                arr[i]+=abs(arr[i-1]-arr[i])+1
            after=arr[i]
            sumi+=after-before
        return sumi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends
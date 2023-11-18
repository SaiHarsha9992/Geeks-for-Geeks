#User function Template for python3
import collections
class Solution:
    def secFrequent(self, arr, n):
        # code here
        d={}
        
        
        
        
        c = collections.Counter(arr)
        v = list(c.values())
        v.sort()
        k=v[-2]
        for i in c:
            if(c[i]==k):
                return i
        
        # print(c)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends

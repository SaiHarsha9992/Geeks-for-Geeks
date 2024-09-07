#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        r = 0
        m = 1 
        while n > 0:
            r += (n%9)*m
            n //= 9
            m *= 10
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends
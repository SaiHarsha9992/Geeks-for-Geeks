#User function Template for python3



class Solution:
    def minNumber(self, arr,n):
        # code here
        sm=sum(arr)
        if sm==1:
            return 1
        def isprime(i):
            if i<=1:
                return False
            j=2
            while j*j<=i:
                if i%j==0:
                    return False
                j+=1
            return True
        for i in range(sm,sm*sm+1):
            if isprime(i):
                return i-sm



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends
